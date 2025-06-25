from config import settings
from common.text_processor import TextProcessor
from common.knowledge_graph import KnowledgeGraph
from common.directory_parser import DirectoryParser
from common.data_processor import DataProcessor
 
 
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
        print(f"Query: {settings.QUERY_TEXT}")
 
        results = kg.run_query("similarity_query", {
            "embedding": embedding,
            "top_k": settings.BANDPASS_TOP_K
        })
 
        for r in results:
            print(f"- {r['name']} (Path: {r['path']}, Similarity: {r['similarity']:.4f})")
 
            neighbors = kg.run_query("get_neighbors", {"path": r["path"]})
            if neighbors:
                print("Neighbors:")
                for n in neighbors:
                    print(f"     → {n['name']} (Path: {n['path']})")
            else:
                print("No neighbors found.")
            print()
 
    elif run_query_name:
        results = kg.run_query(run_query_name)
        for r in results:
            print(r)
 
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
 
if __name__ == "__main__":
    run_task_1()
    run_task_2(run_query_name="similarity_query")
    run_task_3()