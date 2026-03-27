from flask import jsonify, request
from app import app
import repository

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>API de Filmes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 40px;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 10px;
            }
            p {
                margin-bottom: 20px;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: #f8f9fa;
                margin-bottom: 10px;
                padding: 12px;
                border-radius: 6px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .method {
                font-weight: bold;
                padding: 4px 8px;
                border-radius: 4px;
                color: white;
                font-size: 12px;
            }
            .GET { background: #28a745; }
            .POST { background: #007bff; }
            .PUT { background: #ffc107; color: black; }
            .PATCH { background: #6f42c1; }
            .DELETE { background: #dc3545; }

            a {
                text-decoration: none;
                color: #007bff;
                font-weight: bold;
            }

            a:hover {
                text-decoration: underline;
            }

            .endpoint {
                flex-grow: 1;
                margin-left: 15px;
            }

            .footer {
                margin-top: 30px;
                font-size: 12px;
                text-align: center;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎬 API de Filmes</h1>
            <p>
                Bem-vindo à API de gerenciamento de filmes. Utilize os endpoints abaixo para realizar operações de consulta, cadastro, atualização e remoção de dados.
            </p>

            <ul>
                <li>
                    <span class="method GET">GET</span>
                    <span class="endpoint">
                        <a href="/filmes">/filmes</a> — Lista todos os filmes cadastrados
                    </span>
                </li>

                <li>
                    <span class="method GET">GET</span>
                    <span class="endpoint">
                        /filmes/&lt;id&gt; — Retorna um filme específico pelo ID
                    </span>
                </li>

                <li>
                    <span class="method POST">POST</span>
                    <span class="endpoint">
                        /filmes — Cadastra um novo filme (envio via JSON)
                    </span>
                </li>

                <li>
                    <span class="method PUT">PUT</span>
                    <span class="endpoint">
                        /filmes/&lt;id&gt; — Atualiza completamente os dados de um filme
                    </span>
                </li>

                <li>
                    <span class="method PATCH">PATCH</span>
                    <span class="endpoint">
                        /filmes/&lt;id&gt; — Alterna a situação do filme (ativo/inativo)
                    </span>
                </li>

                <li>
                    <span class="method DELETE">DELETE</span>
                    <span class="endpoint">
                        /filmes/&lt;id&gt; — Remove um filme do sistema
                    </span>
                </li>
            </ul>

            <div class="footer">
                Realize a importação do arquivo postman_collection.json para testar as rotas da API.<br>O conteúdo aplicado aqui é de finalidade acadêmica.
                
            </div>
        </div>
    </body>
    </html>
    """

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