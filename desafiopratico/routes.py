from flask import jsonify, request
from app import app
import repository

@app.route("/filmes", methods=['GET'])
def filmes_listar_todos():
    dados = repository.carregar_filmes()
    return jsonify(dados), 200

@app.route("/filmes/<int:id>", methods=['GET'])
def filmes_por_id(id):
    dados = repository.carregar_filmes()
    for filme in dados:
        if filme['id'] == id:
            return jsonify(filme), 200
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=['DELETE'])
def filmes_deletar(id):
    dados = repository.carregar_filmes()
    for filme in dados:
        if filme['id'] == id:
            dados.remove(filme)

            repository.persistir_filmes(dados)
            return jsonify({"info": "Filme removido com sucesso"}), 204
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=['PATCH'])
def filmes_alterar_situacao(id):
    dados = repository.carregar_filmes()
    for filme in dados:
        if filme['id'] == id:
            filme['situacao'] = not filme['situacao']

            repository.persistir_filmes(dados)
            return jsonify(filme), 204
    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=['PUT'])
def filmes_atualizar(id):
    dados = repository.carregar_filmes()
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

            repository.persistir_filmes(dados)
            return jsonify(filme), 200

    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes", methods=['POST'])
def filmes_cadastrar():
    dados = repository.carregar_filmes()
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
    repository.persistir_filmes(dados)

    return jsonify(novo_filme), 201