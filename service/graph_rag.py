import os
import json
from huggingface_hub import InferenceClient
from config.settings import (
    NEO4J_URI,
    NEO4J_USERNAME,
    NEO4J_PASSWORD,
    EMBEDDING_MODEL,
    HF_TOKEN,
    QA_MODEL,
)
from common.knowledge_graph import KnowledgeGraph
from common.text_processor import TextProcessor


class GraphRAG:
    def __init__(
        self,
        hf_token=HF_TOKEN,
        top_k=3,
        neighbors_k=3
    ):
        """Initialize the Graph‑RAG pipeline and Neo4j connection."""
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
            provider="auto",
            api_key=hf_token,
        )

        self.llm_model = QA_MODEL
        self.template = self.load_model_template()

    def load_model_template(self):
        """Load prompt & message structure from model_templates/<model>.json"""
        model_name = self.llm_model.split("/")[-1].lower().replace(" ", "-")
        filename = f"{model_name}.json"
        path = os.path.join("model_templates", filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Model template not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def close(self):
        self.kg.close()

    def chat_interface(self, user_query: str) -> str:
        """Process user query, build context from KG, and use LLM to answer."""
        print(f"\nProcessing query: {user_query}")
        query_embedding = self.text_processor.generate_embedding(user_query)

        top_results = self.kg.run_query("similarity_query", {
            "embedding": query_embedding,
            "top_k": self.top_k
        })

        if not top_results:
            return "No answer found."

        full_context = ""
        used_paths = set()

        for result in top_results:
            path = result.get("path")
            used_paths.add(path)
            main_node = self.kg.get_node_by_path(path)
            if main_node:
                full_context += f"\n[{main_node['name']}]\n{main_node['content']}\n"

            neighbors = self.kg.run_query("get_neighbors", {"path": path})[:self.neighbors_k]
            for neighbor in neighbors:
                n_path = neighbor.get("path")
                if n_path not in used_paths:
                    used_paths.add(n_path)
                    neighbor_node = self.kg.get_node_by_path(n_path)
                    if neighbor_node:
                        full_context += f"\n[{neighbor_node['name']}]\n{neighbor_node['content']}\n"

        if not full_context.strip():
            return "No content available."

        # Build messages using template
        system_prompt = self.template["system_prompt"]
        user_template = self.template["user_template"]

        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": system_prompt}]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": block["type"],
                        "text": block["text"]
                            .replace("{context}", full_context.strip())
                            .replace("{question}", user_query.strip())
                    }
                    for block in user_template
                ]
            }
        ]

        response = self.qa_client.chat.completions.create(
            model=self.llm_model,
            messages=messages
        )

        final_answer = response.choices[0].message.content.strip()
        print("\nAnswer:", final_answer)
        return final_answer
