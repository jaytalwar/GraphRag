import streamlit as st

def render():
    st.title("🏷️ Task 3: NER-based Entity Enrichment")

    st.markdown("""
    ### 🔧 Functionality:
    - Uses spaCy's `en_core_web_trf` model to extract named entities from document sections.
    - Adds entity lists as a property to each `File` and `Section` node.
    - Optionally creates `RELATED_TO` edges between documents based on entity overlap or distance.

    ### ⚙️ How to Run:
    ```bash
    python main.py --task task3 --method distance --min_hops 4
    ```

    ### ⚙️ Parameters:
    - `--method`: `jaccard` or `distance`
    - `--min_hops`: Minimum number of graph-hops between nodes to link with `RELATED_TO`.

    ### 📤 Output:
    - Nodes enriched with `entities: [list of strings]`
    - New semantic `RELATED_TO` edges

    """)

    st.success("✅ Tip: Try visualizing these enriched relationships using Bloom or `streamlit-agraph`.")
