from sentence_transformers import SentenceTransformer
 
class TextProcessor:
 
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """ This method loads the specified SentenceTransformer model into memory so it can be used later to encode text."""
        self.model = SentenceTransformer(model_name)
 
    def generate_embedding(self, text):
        """This method generates a semantic embedding (vector) from the input text using a pre-trained transformer model."""
        if not text.strip():
            return []
        embedding = self.model.encode(text.strip()).tolist()
        return embedding
