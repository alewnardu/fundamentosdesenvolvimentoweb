from flask import jsonify, request
from app import app

dados = [
        {
            "id": 1,
            "titulo": "Harry Potter e a Pedra Filosofal",
            "titulo_original": "Harry Potter and the Sorcerer's Stone",
            "diretor": "Chris Columbus",
            "ano_lancamento": 2001,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 152,
            "classificacao": "Livre",
            "avaliacao_imdb": 7.6,
            "situacao": 1
        },
        {
            "id": 2,
            "titulo": "Harry Potter e a Câmara Secreta",
            "titulo_original": "Harry Potter and the Chamber of Secrets",
            "diretor": "Chris Columbus",
            "ano_lancamento": 2002,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 161,
            "classificacao": "Livre",
            "avaliacao_imdb": 7.4,
            "situacao": 1
        },
        {
            "id": 3,
            "titulo": "Harry Potter e o Prisioneiro de Azkaban",
            "titulo_original": "Harry Potter and the Prisoner of Azkaban",
            "diretor": "Alfonso Cuarón",
            "ano_lancamento": 2004,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 142,
            "classificacao": "Livre",
            "avaliacao_imdb": 7.9,
            "situacao": 1
        },
        {
            "id": 4,
            "titulo": "Harry Potter e o Cálice de Fogo",
            "titulo_original": "Harry Potter and the Goblet of Fire",
            "diretor": "Mike Newell",
            "ano_lancamento": 2005,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 157,
            "classificacao": "12",
            "avaliacao_imdb": 7.7,
            "situacao": 1
        },
        {
            "id": 5,
            "titulo": "Harry Potter e a Ordem da Fênix",
            "titulo_original": "Harry Potter and the Order of the Phoenix",
            "diretor": "David Yates",
            "ano_lancamento": 2007,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 138,
            "classificacao": "12",
            "avaliacao_imdb": 7.5,
            "situacao": 1
        },
        {
            "id": 6,
            "titulo": "Harry Potter e o Enigma do Príncipe",
            "titulo_original": "Harry Potter and the Half-Blood Prince",
            "diretor": "David Yates",
            "ano_lancamento": 2009,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 153,
            "classificacao": "12",
            "avaliacao_imdb": 7.6,
            "situacao": 1
        },
        {
            "id": 7,
            "titulo": "Harry Potter e as Relíquias da Morte: Parte 1",
            "titulo_original": "Harry Potter and the Deathly Hallows – Part 1",
            "diretor": "David Yates",
            "ano_lancamento": 2010,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 146,
            "classificacao": "12",
            "avaliacao_imdb": 7.7,
            "situacao": 1
        },
        {
            "id": 8,
            "titulo": "Harry Potter e as Relíquias da Morte: Parte 2",
            "titulo_original": "Harry Potter and the Deathly Hallows – Part 2",
            "diretor": "David Yates",
            "ano_lancamento": 2011,
            "genero": "Fantasia/Aventura",
            "duracao_minutos": 130,
            "classificacao": "12",
            "avaliacao_imdb": 8.1,
            "situacao": 1
        }
    ]

@app.route("/filmes", methods=['GET'])
def filmes_listar_todos():
    return jsonify(dados), 200

@app.route("/filmes/<int:id>", methods=['GET'])
def filmes_por_id(id):
    for filme in dados:
        if filme['id'] == id:
            return jsonify(filme), 200
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=['DELETE'])
def filmes_deletar(id):
    for filme in dados:
        if filme['id'] == id:
            dados.remove(filme)
            return jsonify({"info": "Filme removido com sucesso"}), 204
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=['PATCH'])
def filmes_alterar_situacao(id):
    for filme in dados:
        if filme['id'] == id:
            filme['situacao'] = not filme['situacao']
            return jsonify(filme), 204
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=['PUT'])
def filmes_atualizar(id):
    dados_recebidos = request.get_json()

    for filme in dados:
        if filme['id'] == id:
            filme['titulo'] = dados_recebidos.get('titulo', filme['titulo'])
            filme['titulo_original'] = dados_recebidos.get('titulo_original', filme['titulo_original'])
            filme['diretor'] = dados_recebidos.get('diretor', filme['diretor'])
            filme['ano_lancamento'] = dados_recebidos.get('ano_lancamento', filme['ano_lancamento'])
            filme['genero'] = dados_recebidos.get('genero', filme['genero'])
            filme['duracao_minutos'] = dados_recebidos.get('duracao_minutos', filme['duracao_minutos'])
            filme['classificacao'] = dados_recebidos.get('classificacao', filme['classificacao'])
            filme['avaliacao_imdb'] = dados_recebidos.get('avaliacao_imdb', filme['avaliacao_imdb'])
            filme['situacao'] = dados_recebidos.get('situacao', filme['situacao'])

            return jsonify(filme), 200

    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes", methods=['POST'])
def filmes_cadastrar():
    dados_recebidos = request.get_json()

    campos_obrigatorios = [
        "titulo",
        "titulo_original",
        "diretor",
        "ano_lancamento",
        "genero",
        "duracao_minutos",
        "classificacao",
        "avaliacao_imdb"
    ]

    for campo in campos_obrigatorios:
        if campo not in dados_recebidos or dados_recebidos[campo] is None:
            return jsonify({"erro": f"Campo obrigatório: {campo}"}), 400

    novo_filme = {
        "id": max([filme['id'] for filme in dados]) + 1 if dados else 1,
        "titulo": dados_recebidos.get("titulo"),
        "titulo_original": dados_recebidos.get("titulo_original"),
        "diretor": dados_recebidos.get("diretor"),
        "ano_lancamento": dados_recebidos.get("ano_lancamento"),
        "genero": dados_recebidos.get("genero"),
        "duracao_minutos": dados_recebidos.get("duracao_minutos"),
        "classificacao": dados_recebidos.get("classificacao"),
        "avaliacao_imdb": dados_recebidos.get("avaliacao_imdb"),
        "situacao": 1,
    }

    dados.append(novo_filme)

    return jsonify(novo_filme), 201