import streamlit as st
 
def render():
    st.title(" CAMS ")
 
    st.markdown("""
    ###  Welcome to CAMS!
 
    This is a unified interface to demonstrate how **markdown-based documentation** can be converted into a **semantic knowledge graph** using:
   
    - Document parsing
    - Knowledge Graph and Semantic Linking
    - Chat Interface
 
    Use the sidebar to explore each task and see live demos and output.
 
    ---
    """)
 
    st.markdown("### Project Goals")
    st.markdown("""
    - Transform unstructured Markdown into a structured **graph-based knowledge base**.
    - Enrich with **NER, embeddings, similarity**, and **relationships**.
    - Enable **question-answering** over product documentation.
 
    """)
 
    st.markdown("###  Technologies Used")
    st.markdown("""
    - **Neo4j**: Graph database
    - **spaCy**: NER and entity linking
    - **SentenceTransformers**: Embeddings
    - **Streamlit**: UI
    - **Hugging Face Inference API**: QA models
    """)
 
    st.info(" Navigate using the sidebar to run and view each task.")