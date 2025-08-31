import os
import streamlit as st
from dotenv import load_dotenv

# Load local .env if it exists (for local dev)
if os.path.exists(".env"):
    load_dotenv()

def get_secret(key: str, default=None):
    """
    Load secrets:
    - Streamlit Cloud → st.secrets
    - Local/dev → os.getenv (from .env or system env)
    """
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key, default)

# Neo4j configuration
NEO4J_URI = get_secret("NEO4J_URI")
NEO4J_USERNAME = get_secret("NEO4J_USER")
NEO4J_PASSWORD = get_secret("NEO4J_PASSWORD")

# Data storage
DATA_DIRECTORY = get_secret("DATA_DIRECTORY", "temp_data")

# Embeddings / NLP
EMBEDDING_MODEL = get_secret("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
SPACY_MODEL_NAME = get_secret("SPACY_MODEL_NAME", "en_core_web_md")

# Query (default example)
QUERY_TEXT = get_secret("QUERY_TEXT", "From where can I see loan arrears?")

# Linking parameters
LINK_METHOD = get_secret("LINK_METHOD", "bandpass")
BANDPASS_MIN_SIM = float(get_secret("BANDPASS_MIN_SIM", 0.2))
BANDPASS_TOP_K = int(get_secret("BANDPASS_TOP_K", 5))
DISTANCE_MIN_SIM = float(get_secret("DISTANCE_MIN_SIM", 0.2))
DISTANCE_MIN_HOPS = int(get_secret("DISTANCE_MIN_HOPS", 5))

# Hugging Face / QA
HF_TOKEN = get_secret("HF_TOKEN")
QA_MODEL = get_secret("QA_MODEL", "meta-llama/Llama-4-Scout-17B-16E-Instruct")
