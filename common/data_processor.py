from typing import List
import spacy
from config.settings import SPACY_MODEL_NAME


class DataProcessor:
    def __init__(self, knowledge_graph):
        """Initialize the DataProcessor with a knowledge graph and load the spaCy NER model."""
        self.kg = knowledge_graph
        self.ner_model = spacy.load(SPACY_MODEL_NAME)  

    def extract_entities(self, text: str) -> List[str]:
        """Extract unique named entities from the given text."""
        doc = self.ner_model(text)
        return list(set(ent.text for ent in doc.ents if ent.label_))

    def enrich_nodes_with_entities(self):
        """Extract NER entities from all file nodes and store them as a property in the graph."""
        nodes = self.kg.get_all_document_nodes()
        for node in nodes:
            entities = self.extract_entities(node.get("content", ""))
            self.kg.run_query("update_node_property", {
                "path": node["path"],
                "key": "ner_entities",
                "value": entities
            })

    def run(self):
        """Run the enrichment process for all document nodes in the knowledge graph."""
        self.enrich_nodes_with_entities()
