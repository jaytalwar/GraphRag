import os
import argparse
from dotenv import load_dotenv
import streamlit as st
 
from config import settings
from common.text_processor import TextProcessor
from common.knowledge_graph import KnowledgeGraph
from common.directory_parser import DirectoryParser
from common.data_processor import DataProcessor
from service.graph_rag import GraphRAG
 
from ui import home_ui, task1_ui, task2_ui, task4_ui  
 
load_dotenv()
 
# -------------------- TASK RUNNERS --------------------
 
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
            kg.run_query("get_neighbors", {"path": r["path"]})
    elif run_query_name:
        kg.run_query(run_query_name)
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
            print(" Exiting.")
            break
        rag.chat_interface(query)
    rag.close()
 
 
# -------------------- STREAMLIT UI --------------------
 
def run_ui():
    st.set_page_config(page_title="CAMS", layout="wide")
 
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #d6f5df;
        border-right: 2px solid #bde5ce;
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        color: #0a4f2e;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        margin-bottom: 0.5rem;
        background-color: #198754;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
 
    if "selected_task" not in st.session_state:
        st.session_state.selected_task = "Home"
 
    with st.sidebar:
        
        st.image("assets/logo.png", use_container_width=True)
 
 
        st.markdown(
            '<div class="sidebar-title" style="text-align: center;">CAMS Tasks</div>',
            unsafe_allow_html=True
            )
 
        if st.button(" Home"):
            st.session_state.selected_task = "Home"
        if st.button(" Document Parsing"):
            st.session_state.selected_task = "Task 1"
        if st.button(" Knowledge Graph and Semantic Linking"):
            st.session_state.selected_task = "Task 2"
        if st.button(" Chat Interface"):
            st.session_state.selected_task = "Task 4"
 
    
    if st.session_state.selected_task == "Task 1":
        task1_ui.render()
    elif st.session_state.selected_task == "Task 2":
        task2_ui.render()
    elif st.session_state.selected_task == "Task 4":
        task4_ui.render()
    else:
        home_ui.render()
 
 
# -------------------- ENTRY POINT --------------------
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, help="task1, task2, task4, ui")
    parser.add_argument("--query_name", type=str, default=None)
 
    args = parser.parse_args()
 
    if args.task == "task1":
        run_task_1()
    elif args.task == "task2":
        run_task_2(args.query_name)
    elif args.task == "task4":
        run_task_4_cli()
    elif args.task == "ui":
        run_ui()
    else:
        print("Invalid task name. Use: task1 | task2 | task4 | ui")
 
 