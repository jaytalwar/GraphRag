import os
from huggingface_hub import InferenceClient
from config.settings import (
    NEO4J_URI,
    NEO4J_USERNAME,
    NEO4J_PASSWORD,
    EMBEDDING_MODEL,
    QA_MODEL,
    HF_TOKEN
)
from common.knowledge_graph import KnowledgeGraph
from common.text_processor import TextProcessor
 
class GraphRAG:
    def __init__(
        self,
        hf_model_name=QA_MODEL,
        hf_token=HF_TOKEN,
        top_k=3,
        neighbors_k=3
    ):
        """Initialize the Graph‑RAG pipeline, models, and Neo4j connection."""
        self.top_k = top_k
        self.neighbors_k = neighbors_k
        self.text_processor = TextProcessor(EMBEDDING_MODEL)
 
        self.kg = KnowledgeGraph(
            uri=NEO4J_URI,
            username=NEO4J_USERNAME,
            password=NEO4J_PASSWORD,
            data_directory=None,
            text_processor=self.text_processor
        )
 
        self.qa_client = InferenceClient(
            model=hf_model_name,
            token=hf_token
        )
 
    def close(self):
        """Gracefully close the Neo4j session."""
        self.kg.close()
 