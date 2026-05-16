from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def gerar_embedding(texto: str):
    if not texto:
        return None

    return model.encode(texto).tolist()


def gerar_embeddings_chunks(chunks):
    embeddings = []

    for i, chunk in enumerate(chunks):
        emb = gerar_embedding(chunk["text"])

        embeddings.append({
            "id": i,
            "embedding": emb,
            "text": chunk["text"],
            "page": chunk["page"]
        })

    return embeddings