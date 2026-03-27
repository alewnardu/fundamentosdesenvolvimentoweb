import json

ARQUIVO_FILMES = "filmes.json"

def carregar_filmes():
    try:
        with open(ARQUIVO_FILMES, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except:
        return []

def persistir_filmes(filmes):
    try:
        with open(ARQUIVO_FILMES, "w", encoding="utf-8") as arquivo:
            json.dump(filmes, arquivo, ensure_ascii=False, indent=4)
    except:
        pass