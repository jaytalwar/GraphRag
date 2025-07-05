import streamlit as st

def render():
    st.title("🧠 Task 2: Knowledge Graph Construction")

    st.markdown("""
    ### 🔧 Functionality:
    - Loads the structured JSON generated in Task 1.
    - Creates `File`, `Section`, and `Subsection` nodes in Neo4j.
    - Establishes `HAS_SECTION`, `HAS_SUBSECTION`, and `PARENT_OF` relationships.

    ### ⚙️ How to Run:
    ```bash
    python main.py --task task2
    ```

    ### 📁 Requirements:
    - Ensure Neo4j is running and connection details are correct in `.env`.
    - Make sure the `parsed_data.json` file from Task 1 exists.

    ### 📤 Output:
    - Visual knowledge graph stored in Neo4j with structural relationships.
    """)

    st.success("✅ Tip: You can preview the graph in Neo4j Browser at http://localhost:7474.")
