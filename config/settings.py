import os
from dotenv import load_dotenv
 
load_dotenv()
 
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
DATA_DIRECTORY = "temp_data"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
SPACY_MODEL_NAME = os.getenv("SPACY_MODEL_NAME", "en_core_web_md")
QUERY_TEXT = os.getenv("QUERY_TEXT", "From where can I see loan arrears?")
LINK_METHOD = os.getenv("LINK_METHOD", "distance")
BANDPASS_MIN_SIM = float(os.getenv("BANDPASS_MIN_SIM", 0.2))
BANDPASS_TOP_K = int(os.getenv("BANDPASS_TOP_K", 5))
DISTANCE_MIN_SIM = float(os.getenv("DISTANCE_MIN_SIM", 0.2))
DISTANCE_MIN_HOPS = int(os.getenv("DISTANCE_MIN_HOPS", 5))