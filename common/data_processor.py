from typing import Dict, Set, List, Tuple
import spacy
from collections import Counter, defaultdict
from config.settings import SPACY_MODEL_NAME
 
 
class DataProcessor:
    def __init__(self, knowledge_graph):
        """Initialize the processor with the knowledge graph and load spaCy model."""
        self.kg = knowledge_graph
        self.ner_model = spacy.load(SPACY_MODEL_NAME)
        self.node_entities: Dict[str, Set[str]] = {}
        self.global_entity_freq: Counter = Counter()
        self.filtered_entities: Set[str] = set()
 
    def extract_entities(self, text: str) -> Set[str]:
        """Extract named entities from text using spaCy NER model."""
        doc = self.ner_model(text or "")
        return {ent.text.strip() for ent in doc.ents if ent.label_}
 
    def enrich_nodes_with_entities(self):
        """Extract and store entities per node, update in Neo4j if not already stored."""
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
        """Filter common or noisy entities using frequency-based bandpass."""
        if not self.global_entity_freq:
            return
 
        sorted_freq = self.global_entity_freq.most_common()
        max_index = int(len(sorted_freq) * max_percentile)
 
        for i, (entity, freq) in enumerate(sorted_freq):
            if freq >= min_freq and i <= max_index:
                self.filtered_entities.add(entity)
 
    def compute_jaccard_similarity(self, set1: Set[str], set2: Set[str]) -> float:
        """Compute Jaccard similarity between two entity sets."""
        if not set1 or not set2:
            return 0.0
        return len(set1 & set2) / len(set1 | set2)
 
    def create_links_with_bandpass_filter(self, top_k: int = 5, min_sim: float = 0.2):
        """Create RELATED_TO links for documents with high entity overlap using bandpass filter."""
        paths = list(self.node_entities.keys())
        doc_sim_scores: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        created_links: Set[Tuple[str, str]] = set()
 
        for i, p1 in enumerate(paths):
            ents1 = self.node_entities[p1] & self.filtered_entities
            if not ents1:
                continue
 
            for j in range(i + 1, len(paths)):
                p2 = paths[j]
                ents2 = self.node_entities[p2] & self.filtered_entities
                if not ents2:
                    continue
 
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
                if (p1, p2) in created_links or (p2, p1) in created_links:
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
 
    def create_links_with_distance_filter(self, min_sim: float = 0.2, min_hops: int = 4):
        """Create RELATED_TO links only if the nodes are semantically similar and graph-distant."""
        paths = list(self.node_entities.keys())
        created_links: Set[Tuple[str, str]] = set()
 
        for i, p1 in enumerate(paths):
            ents1 = self.node_entities[p1] & self.filtered_entities
            if not ents1:
                continue
 
            for j in range(i + 1, len(paths)):
                p2 = paths[j]
                ents2 = self.node_entities[p2] & self.filtered_entities
                if not ents2:
                    continue
 
                sim = self.compute_jaccard_similarity(ents1, ents2)
                if sim < min_sim:
                    continue
 
                result = self.kg.run_query("get_shortest_path_length", {
                    "path1": p1,
                    "path2": p2
                })
 
                if not result:
                    continue
 
                path_length = result[0].get("length", 0)
                if path_length < min_hops:
                    continue
 
                if (p1, p2) in created_links or (p2, p1) in created_links:
                    continue
 
                self.kg.run_query("create_related_to", {
                    "path1": p1,
                    "path2": p2
                })
 
                created_links.add((p1, p2))
 
    def run(self, method: str = "bandpass", **kwargs):
          """Run full pipeline: extract, filter, link nodes."""
        self.enrich_nodes_with_entities()
        self.filter_entities_by_frequency(min_freq=2, max_percentile=0.9)
 
        if method == "bandpass":
            self.create_links_with_bandpass_filter(
                top_k=kwargs.get("top_k", 5),
                min_sim=kwargs.get("min_sim", 0.2)
            )
        elif method == "distance":
            self.create_links_with_distance_filter(
                min_sim=kwargs.get("min_sim", 0.2),
                min_hops=kwargs.get("min_hops", 5)
            )