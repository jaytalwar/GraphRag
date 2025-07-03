import os
from dotenv import load_dotenv
from config import settings
from common.text_processor import TextProcessor
from common.knowledge_graph import KnowledgeGraph
from common.directory_parser import DirectoryParser
from common.data_processor import DataProcessor
from service.graph_rag import GraphRAG

load_dotenv()

def run_task_1():
    parser = DirectoryParser()
    parser.parse()

def run_task_2(run_query_name=None):
    processor = TextProcessor()
    kg = KnowledgeGraph(
        uri=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
        data_directory=settings.DATA_DIRECTORY,
        text_processor=processor
    )

    kg.build_graph()

    dp = DataProcessor(kg)
    dp.run(
        method=settings.LINK_METHOD,
        top_k=settings.BANDPASS_TOP_K,
        min_sim=settings.BANDPASS_MIN_SIM,
        min_hops=settings.DISTANCE_MIN_HOPS
    )

    if run_query_name == "similarity_query":
        embedding = processor.generate_embedding(settings.QUERY_TEXT)
        results = kg.run_query("similarity_query", {
            "embedding": embedding,
            "top_k": settings.BANDPASS_TOP_K
        })

        for r in results:
            neighbors = kg.run_query("get_neighbors", {"path": r["path"]})

    elif run_query_name:
        results = kg.run_query(run_query_name)

    kg.close()

def run_task_3():
    processor = TextProcessor()
    kg = KnowledgeGraph(
        uri=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
        data_directory=settings.DATA_DIRECTORY,
        text_processor=processor
    )
    dp = DataProcessor(kg)
    dp.run(
        method=settings.LINK_METHOD,
        top_k=settings.BANDPASS_TOP_K,
        min_sim=settings.BANDPASS_MIN_SIM,
        min_hops=settings.DISTANCE_MIN_HOPS
    )
    kg.close()


def run_task_4_cli():
    rag = GraphRAG(
        hf_token=settings.HF_TOKEN,
        top_k=3,
        neighbors_k=3
    )

    print(" Ask me anything about the graph-based knowledge base.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Question: ").strip()
        if query.lower() in {"exit", "quit"}:
            print("👋 Exiting.")
            break

        rag.chat_interface(query)

    rag.close()

if __name__ == "__main__":
    run_task_1()
    run_task_2(run_query_name="similarity_query")
    run_task_3()
    run_task_4_cli()
