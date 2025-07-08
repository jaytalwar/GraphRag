import json
import streamlit as st
from service.graph_rag import GraphRAG
from config import settings
import sentence_transformers as st_models
 
original_sentence_transformer = st_models.SentenceTransformer
 
def sentence_transformer_cpu(model_name, *args, **kwargs):
    """Force model to load on CPU."""
    kwargs["device"] = "cpu"
    return original_sentence_transformer(model_name, *args, **kwargs)
 
st_models.SentenceTransformer = sentence_transformer_cpu
 
def rerun():
    """Force Streamlit to rerun the app."""
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
 
def get_rag() -> GraphRAG:
    """Get or create the GraphRAG instance in session state."""
    if "rag" not in st.session_state:
        st.session_state.rag = GraphRAG(
            hf_token=settings.HF_TOKEN,
            top_k=3,
            neighbors_k=3,
        )
        st.session_state.chat_turns = []
    return st.session_state.rag
 
def render():
    """Render the chat UI and handle user interaction."""
    st.title("Ask Me Anything About Your Docs!")
    rag = get_rag()
 
    for question, answer, prompt in st.session_state.chat_turns:
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            st.write(answer)
            with st.expander("📝 Prompt + context", expanded=False):
                st.code(prompt, language="json")
 
    user_query = st.chat_input("Ask your question…")
 
    if user_query:
        captured = {"prompt": None}
        original_generate = rag.generate_messages
 
        def capture_messages(*args, **kwargs):
            """Capture the prompt used to generate the response."""
            captured["prompt"] = original_generate(*args, **kwargs)
            return captured["prompt"]
 
        rag.generate_messages = capture_messages
 
        with st.spinner("Thinking…"):
            assistant_answer = rag.chat_interface(user_query)
 
        rag.generate_messages = original_generate
 
        prompt_json = (
            json.dumps(captured["prompt"], indent=2, ensure_ascii=False)
            if captured["prompt"]
            else "⟨prompt not captured⟩"
        )
 
        st.session_state.chat_turns.append((user_query, assistant_answer, prompt_json))
        rerun()
 
    if st.session_state.get("chat_turns") and st.button("🗑️ Clear chat"):
        """Clear the chat history and reset GraphRAG memory."""
        st.session_state.chat_turns = []
        st.session_state.rag.clear_history()
        rerun()