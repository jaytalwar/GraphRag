from config import settings
from common.text_processor import TextProcessor
from common.knowledge_graph import KnowledgeGraph
from common.directory_parser import DirectoryParser
from common.data_processor import DataProcessor


def run_task_1():
    print("[TASK 1] Starting directory parsing...")
    parser = DirectoryParser()
    parser.parse()
    print("[TASK 1] Directory parsing completed.\n")


def run_task_2(run_query_name=None):
    print("[TASK 2] Initializing components...")
    processor = TextProcessor()

    kg = KnowledgeGraph(
        uri=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
        data_directory=settings.DATA_DIRECTORY,
        text_processor=processor
    )

    print("[TASK 2] Building knowledge graph...")
    kg.build_graph()
    print("[TASK 2] Graph built successfully.\n")

    dp = DataProcessor(kg)
    dp.run()

    if run_query_name == "similarity_query":
        query_text = "From where can I see loan arrears?"
        print("[TASK 2] Running similarity query for:", query_text)
        embedding = processor.generate_embedding(query_text)
        results = kg.run_query("similarity_query", {"embedding": embedding, "top_k": 3})

        print("[TASK 2] Similarity Query Results:")
        for r in results:
            print(f"- {r['name']} (Path: {r['path']}, Similarity: {r['similarity']:.4f})")

            # Fetch and print the top 5 neighbors for each result
            neighbors = kg.run_query("get_neighbors", {"path": r["path"]})
            if neighbors:
                print("  Top 5 Neighbors:")
                for n in neighbors:
                    print(f"   • {n['name']} (Path: {n['path']})")
            else:
                print("  No neighbors found.")
            print()

    elif run_query_name:
        print(f"[TASK 2] Running named query: {run_query_name}")
        results = kg.run_query(run_query_name)
        print(f"[TASK 2] Results for query '{run_query_name}':")
        for r in results:
            print(r)

    kg.close()
    print("[TASK 2] Closed database connection.\n")


def run_task_3():
    print("[TASK 3] Starting entity-based link generation...\n")

    processor = TextProcessor()

    kg = KnowledgeGraph(
        uri=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
        data_directory=settings.DATA_DIRECTORY,
        text_processor=processor
    )

    dp = DataProcessor(kg)
    dp.run()

    kg.close()
    print("[TASK 3] Entity-based link generation completed.\n")


if __name__ == "__main__":
    print("========== STARTING PIPELINE ==========\n")
    run_task_1()
    run_task_2(run_query_name="similarity_query")
    run_task_3()
    print("========== PIPELINE EXECUTION COMPLETE ==========")
