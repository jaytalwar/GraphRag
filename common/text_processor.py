from sentence_transformers import SentenceTransformer

class TextProcessor:

    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """Load the specified SentenceTransformer model into memory for text encoding."""
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text):
        """Generate a semantic embedding (vector) from the input text using the loaded model."""
        if not text.strip():
            return []
        embedding = self.model.encode(text.strip()).tolist()
        return embedding
