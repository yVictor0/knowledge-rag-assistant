import numpy as np
from src.core.embedding import gerar_embedding


def buscar_contexto(pergunta, index, dados, k=3):

    emb_pergunta = gerar_embedding(pergunta)

    if not emb_pergunta:
        return "Erro ao gerar embedding da pergunta."

    vetor = np.array([emb_pergunta]).astype("float32")

    distancias, indices = index.search(vetor, k)

    resultados = []

    for i in indices[0]:

        if 0 <= i < len(dados):
            chunk = dados[i]

            resultados.append(
                f"(Página {chunk['page']}) {chunk['text']}"
            )


    if not resultados:
        return "Nenhum contexto relevante encontrado."

    return "\n\n".join(resultados)