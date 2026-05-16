import faiss
import numpy as np
from src.utils.store import carregar_embeddings


def criar_index():
    dados = carregar_embeddings()

    vetores = [item["embedding"] for item in dados]
    matriz = np.array(vetores).astype("float32")

    dim = matriz.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(matriz)

    return index, dados