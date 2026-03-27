# PROGRAMAÇÃO PARA WEB I
Repositório da Disciplina Programação para Web I (TADS - 3º Período - PALMAS)

### Projeto 03 - Desafio Prático

A aplicação está escrita em Pyhton e Flask, permitindo realizar operações de
CRUD (Create, Read, Update, Delete) utilizando persistência em arquivo
JSON no contexto da entidade Filme.

#### Estrutura do Projeto

    desafiopratico/
    │
    ├── venv/                     # Ambiente virtual Python
    ├── app.py                   # Arquivo principal da aplicação Flask
    ├── routes.py                # Definição das rotas/endpoints da API
    ├── repository.py            # Camada de acesso aos dados (leitura/escrita JSON)
    ├── filmes.json              # Base de dados em formato JSON
    ├── postman_collection.json  # Coleção de endpoints para testes no Postman
    ├── requirements.txt         # Dependências do projeto
    └── .gitignore               # Arquivos ignorados pelo Git

#### Como executar o projeto

#### 1. Criar e ativar o ambiente virtual

#### Windows

    python -m venv venv
    venv\Scripts\activate

#### Linux/Mac

    python3 -m venv venv
    source venv/bin/activate

#### 2. Instalar as dependências

    pip install -r requirements.txt

#### 3. Executar a aplicação

    python app.py

A aplicação será iniciada em: http://127.0.0.1:5000

#### Endpoints da API

  Método    Rota    Descrição
  -------- -------------- -----------------------
  GET      /filmes        Lista todos os filmes  
  GET      /filmes/{id}   Busca filme por ID  
  POST     /filmes        Cadastra novo filme  
  PUT      /filmes/{id}   Atualiza filme  
  PATCH    /filmes/{id}   Atualiza parcialmente o filme  
  DELETE   /filmes/{id}   Remove filme  

#### Testes com Postman

O arquivo `postman_collection.json` pode ser importado no Postman para
facilitar os testes dos endpoints.

### Projeto 02

Clique no link de visualização da página projeto02.html:
https://alewnardu.github.io/fundamentosdesenvolvimentoweb/projeto02/projeto02.html

![Preview do Projeto](projeto02/images/projeto02.png)

### Projeto 01

Clique no link de visualização da página projeto01.html:
https://alewnardu.github.io/fundamentosdesenvolvimentoweb/projeto01/projeto01.html

![Preview do Projeto](projeto01/images/projeto01.png)