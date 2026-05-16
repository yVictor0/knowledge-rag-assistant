from pathlib import Path
import os

from src.utils.pdf_loader import extract_text_from_pdf, chunk_text
from src.core.embedding import gerar_embeddings_chunks
from src.utils.store import salvar_embeddings
from src.core.vector_store import criar_index
from src.services.ia import responder


def build_base():
    BASE_DIR = Path(__file__).resolve().parent
    pdf_path = BASE_DIR / "data" / "pdfs" / "documento1.pdf"

    if not pdf_path.exists():
        print(f"PDF não encontrado: {pdf_path}")
        return


    pages = extract_text_from_pdf(str(pdf_path))
    print(f"Páginas lidas: {len(pages)}")


    chunks = chunk_text(pages)
    print(f"Chunks: {len(chunks)}")

    if not chunks:
        print("Nenhum chunk gerado.")
        return

    print("Gerando embeddings...")
    dados = gerar_embeddings_chunks(chunks)

    if not dados:
        print("Erro ao gerar embeddings.")
        return

    salvar_embeddings(dados)
    print("Base criada com sucesso!")


def chat():
    try:
        index, dados = criar_index()
    except FileNotFoundError:
        print("Você precisa primeiro construir a base (opção 1).")
        return

    historico = []

    print("\nDigite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit"]:
            break


        historico.append(f"Usuário: {pergunta}")

        resposta = responder(pergunta, index, dados, historico)


        historico.append(f"Assistente: {resposta}")

        print("\nBot:", resposta)
        print("-" * 50)

if __name__ == "__main__":
    print("1 - Construir base")
    print("2 - Conversar")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        build_base()
    elif opcao == "2":
        chat()
    else:
        print("Opção inválida.")