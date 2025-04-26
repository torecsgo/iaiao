import numpy as np
from sentence_transformers import SentenceTransformer

class RAG:
    def __init__(self, corpus):
        self._corpus = corpus
        self._model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self._chunks = self.__split_corpus__()
        self._chunks_embeddings = self.__add_chunk_embeddings__()

    def __split_corpus__(self, chunk_size=500, overlap_size=50):
        # Dividir el corpus en palabras
        palabras = self._corpus.split()

        chunks = []
        start = 0

        while start < len(palabras):
            # Definir el final del chunk
            end = start + chunk_size

            # Extraer el chunk y unir las palabras de nuevo en un texto
            chunk = palabras[start:end]
            chunks.append(' '.join(chunk))

            # Actualizar el inicio del siguiente chunk considerando el solape
            start = end - overlap_size

        return chunks
    
    def __add_chunk_embeddings__(self):
        chunks_embeddings = {}
        for i, chunk in enumerate(self._chunks):
            embedding = self.get_embedding(chunk)
            chunks_embeddings[i] = {'text': chunk, 'embedding': embedding}
        return chunks_embeddings
    
    def get_embedding(self, text: str):
        # Obtener el embedding utilizando el modelo cargado
        return self._model.encode(text)

    def get_closest_reply(self, embedding1: np.ndarray):
        resultados = []
        for key in self._chunks_embeddings:
            embedding2 = self._chunks_embeddings[key]['embedding']

            # Calcular el producto punto entre los dos embeddings
            dot_product = np.dot(embedding1, embedding2)

            # Calcular las normas de los dos embeddings
            norm_embedding1 = np.linalg.norm(embedding1)
            norm_embedding2 = np.linalg.norm(embedding2)

            # Calcular la similitud de coseno
            cosine_similarity = dot_product / (norm_embedding1 * norm_embedding2)
            resultados.append([key, cosine_similarity, self._chunks_embeddings[key]['text']])

        # Ordenar los resultados de mayor a menor similitud
        resultados.sort(key=lambda x: x[1], reverse=True)
        return resultados