from config import settings
from common.text_processor import TextProcessor
from common.knowledge_graph import KnowledgeGraph
from common.directory_parser import DirectoryParser

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

    if run_query_name == "similarity_query":
        query_text = "From where can I see loan arrears?" 
        print(query_text)
        embedding = processor.generate_embedding(query_text)
        results = kg.run_query("similarity_query", {"embedding": embedding, "top_k": 3})
        print(" Similarity Query Results:")
        for r in results:
            print(r)

    elif run_query_name:
        results = kg.run_query(run_query_name)
        print(f" Results for query '{run_query_name}':")
        for r in results:
            print(r)

    kg.close()

if __name__ == "__main__":
    run_task_1()
    run_task_2(run_query_name="similarity_query")
    

    