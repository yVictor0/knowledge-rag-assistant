import ollama
from src.core.contexto import buscar_contexto


def responder(pergunta, index, dados, historico=None):
    contexto = buscar_contexto(pergunta, index, dados)

    historico_texto = "\n".join(historico[-6:]) if historico else ""

    prompt = f"""
Você é um assistente inteligente.

Use APENAS o contexto abaixo.

Histórico:
{historico_texto}

Contexto:
{contexto}

Pergunta:
{pergunta}

Se não souber, diga que não sabe.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]