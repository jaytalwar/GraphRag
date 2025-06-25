from typing import List, Dict, Set, Tuple
import spacy
from collections import Counter, defaultdict
from config.settings import SPACY_MODEL_NAME


class DataProcessor:
    def __init__(self, knowledge_graph):
        self.kg = knowledge_graph
        self.ner_model = spacy.load(SPACY_MODEL_NAME)
        self.node_entities: Dict[str, Set[str]] = {}
        self.global_entity_freq: Counter = Counter()
        self.filtered_entities: Set[str] = set()

    def extract_entities(self, text: str) -> Set[str]:
        doc = self.ner_model(text or "")
        return {ent.text.strip() for ent in doc.ents if ent.label_}

    def enrich_nodes_with_entities(self):
        nodes = self.kg.get_all_document_nodes()

        for node in nodes:
            path = node["path"]
            stored_entities = node.get("ner_entities")
            if stored_entities:
                entities = set(stored_entities)
            else:
                entities = self.extract_entities(node.get("content", ""))

            if not entities:
                continue

            self.node_entities[path] = entities
            self.global_entity_freq.update(entities)

            if not stored_entities:
                self.kg.run_query("update_node_property", {
                    "path": path,
                    "key": "ner_entities",
                    "value": list(entities)
                })

    def filter_entities_by_frequency(self, min_freq=2, max_percentile=0.9):
        if not self.global_entity_freq:
            return

        sorted_freq = self.global_entity_freq.most_common()
        max_index = int(len(sorted_freq) * max_percentile)

        for i, (entity, freq) in enumerate(sorted_freq):
            if freq >= min_freq and i <= max_index:
                self.filtered_entities.add(entity)

    def compute_jaccard_similarity(self, set1: Set[str], set2: Set[str]) -> float:
        if not set1 or not set2:
            return 0.0
        return len(set1 & set2) / len(set1 | set2)

    def create_doc_links_by_filtered_similarity(self, top_k: int = 5, min_sim: float = 0.2):
        paths = list(self.node_entities.keys())
        doc_sim_scores: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        created_links: Set[Tuple[str, str]] = set()

        for i, p1 in enumerate(paths):
            ents1 = self.node_entities[p1] & self.filtered_entities
            for j in range(i + 1, len(paths)):
                p2 = paths[j]
                ents2 = self.node_entities[p2] & self.filtered_entities
                sim = self.compute_jaccard_similarity(ents1, ents2)
                if sim >= min_sim:
                    doc_sim_scores[p1].append((p2, sim))
                    doc_sim_scores[p2].append((p1, sim))

        links_per_doc = defaultdict(int)
        for p1, neighbors in doc_sim_scores.items():
            neighbors = sorted(neighbors, key=lambda x: x[1], reverse=True)
            for p2, sim in neighbors:
                if links_per_doc[p1] >= top_k or links_per_doc[p2] >= top_k:
                    continue
                if (p2, p1) in created_links or (p1, p2) in created_links:
                    continue
                self.kg.run_query("create_related_to", {
                    "path1": p1,
                    "path2": p2
                })
                created_links.add((p1, p2))
                links_per_doc[p1] += 1
                links_per_doc[p2] += 1
                if links_per_doc[p1] >= top_k:
                    break

    def run(self):
        self.enrich_nodes_with_entities()
        self.filter_entities_by_frequency(min_freq=2, max_percentile=0.9)
        self.create_doc_links_by_filtered_similarity(top_k=5, min_sim=0.2)
