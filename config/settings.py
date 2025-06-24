import os
from dotenv import load_dotenv
 
load_dotenv()
 
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
DATA_DIRECTORY = "temp_data"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
SPACY_MODEL_NAME = os.getenv("SPACY_MODEL_NAME", "en_core_web_md")