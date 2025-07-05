import streamlit as st

def render():
    st.title("🧠 Task 4: GraphRAG-based QA")

    st.markdown("""
    ### 🔧 Functionality:
    - Implements a hybrid retrieval pipeline combining:
        - Graph-based filtering (e.g., via RELATED_TO links or paths)
        - Embedding-based similarity search
    - Uses a Hugging Face-hosted LLM (e.g., Mistral, LLaMA) to answer natural queries using context from relevant nodes.

    ### ⚙️ How to Run:
    ```bash
    python main.py --task task4 --query "How to update KYC?"
    ```

    ### 🛠️ Requirements:
    - Set `QA_MODEL` and `HF_TOKEN` in `.env`
    - Ensure `GraphRAG` is correctly configured with your graph and text processor

    ### 📤 Output:
    - Final answer from LLM
    - List of retrieved contexts from the graph
    - Optional metadata like source file, entities

    """)

    st.success("✅ Tip: Use `streamlit` interface in Task 5 for demo-ready QA system.")
