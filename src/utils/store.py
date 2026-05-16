from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # volta até raiz do projeto
CAMINHO_PADRAO = BASE_DIR / "embeddings.json"


def salvar_embeddings(dados, caminho=CAMINHO_PADRAO):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f)


def carregar_embeddings(caminho=CAMINHO_PADRAO):
    if not os.path.exists(caminho):
        raise FileNotFoundError("Arquivo embeddings.json não encontrado.")

    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)