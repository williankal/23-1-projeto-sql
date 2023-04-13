# 23-1-projeto-sql-pedroandrade-umdadofilosofal
23-1-projeto-sql-pedroandrade-umdadofilosofal created by GitHub Classroom


# Projeto 1 SQL - API de gerenciamento de filmes

Alunos: 
- Pedro Henrique Britto Aragão Andrade
- Willian Kenzo

## API de Filmes e Avaliações
A API de Filmes e Avaliações é uma aplicação em Python que utiliza o framework FastAPI para criar uma API para gerenciar filmes e suas avaliações.

A aplicação possui dois modelos de dados: Filme e Avaliacao. O modelo Filme possui os atributos `id_filme` (identificador único do filme), `name` (nome do filme) e `description` (descrição do filme). Já o modelo Avaliacao possui os atributos `id_avaliacao` (identificador único da avaliação), `description` (descrição da avaliação), `nota` (nota do filme) e `id_filme` (identificador do filme avaliado). Ambos os modelos utilizam o método `Field` da biblioteca pydantic para validar os dados.

A base de dados é um dicionário em memória chamado `banco` que armazena a lista de filmes e avaliações cadastrados. A lista de filmes é armazenada em `banco["filmes"]` e a lista de avaliações é armazenada em `banco["avaliacoes"]`.

### Tabela de Filmes

Esta tabela armazena informações sobre os filmes cadastrados no sistema. Cada registro da tabela representa um filme cadastrado, contendo informações como o ID do filme, name, descrição.

Estrutura da tabela
A tabela de filmes possui as seguintes colunas:

- `id_filme`: identificador único do filme (inteiro).
- `name`: título do filme (texto).
- `description`: descrição do filme (texto).

#### Rotas:

- `GET /filmes`: Retorna a lista de todos os filmes cadastrados no sistema.
- `GET /filmes/{id_filme}`: Retorna os detalhes do filme com o ID especificado.
- `POST /filmes/adiciona`: Adiciona um novo filme ao sistema.
- `PUT /filmes/{id_filme}`: Atualiza as informações do filme com o ID especificado.
- `DELETE /filmes/{id_filme}`: Remove o filme com o ID especificado do sistema.

### Listar todos os Filmes
Rota: `GET /filmes`

Lista todos os filmes presentes no banco de dados.

Parâmetros:

- Não necessita de parâmetros.

Retorno de exemplo:

```` py
[
  {
    "id_filme": 0,
    "name": "Pedro Aragão",
    "description": "Filme sobre o Pedro Aragão"
  },
  {
    "id_filme": 1,
    "name": "Pedro Aragão 2",
    "description": "Filme sobre o Pedro Aragão 2"
  },
  {
    "id_filme": 2,
    "name": "Pedro Aragão 3",
    "description": "Filme sobre o Pedro Aragão 3"
  }
]
````

### Listar um Filme em específico
Rota: `GET /filmes/{id_filme}`

Lista um filme em específico.

Parâmetros:

- `id_filme` (obrigatório): ID do filme que será listado.

Retorno de exemplo:

- Entradas: id_filme = 0

```` py
[
  {
    "id_filme": 0,
    "name": "Pedro Aragão",
    "description": "Filme sobre o Pedro Aragão"
  }
]
````

### Adicionar Filme
Rota: `POST /filmes/adiciona`

Adiciona um novo filme ao banco de dados.

Parâmetros:

- `name` (obrigatório): Nome do filme a ser adicionado.
- `description` (opcional): Descrição do filme a ser adicionado.

Retorno de exemplo:

- Entrada: name = Pedro o poderoso chefinho; description: null.

```` py
[
  {
    "id_filme": 3,
    "name": "Pedro o poderoso chefinho",
    "description": null
  }
]
````

- Retorna os dados do filme adicionado se a operação for bem-sucedida.

### Atualizar Filme
Rota: `PUT /filmes/{id_filme}`

Atualiza os dados de um filme específico pelo seu ID.

Parâmetros:

- `id_filme` (obrigatório): ID do filme a ser atualizado.
- `name` (opcional): Novo nome do filme.
- `description` (opcional): Nova descrição do filme.

Retorno de exemplo:

- Entrada: id_filme = 1; name = Pedro o infalível; description = Filme muito bom;

```` py
[
  {
    "id_filme": 1,
    "name": "Pedro o infalível",
    "description": "Filme muito bom"
  }
]
````

- Retorna os dados do filme atualizado se a operação for bem-sucedida.

### Deleta Filme
Rota: `DELETE /filmes/{id_filme}`

Deleta um filme em específico.

Parâmetros:

- `id_filme` (obrigatório): ID do filme a ser deletado.

Retorno de exemplo:

- Entrada: id_filme = 0.

```` py
[
  {
    "detail": "filme deletado"
  }
]
````

- Retorna que o filme foi deletado se a operação for bem-sucedida.

### Tabela de Avaliacoes

Esta tabela armazena informações sobre as avaliações cadastrados no sistema. Cada registro da tabela representa uma avaliação cadastrada, contendo informações como o ID da avaliação, descrição, nota e ID do filme.

Estrutura da tabela
A tabela de filmes possui as seguintes colunas:

- `id_avaliacao`: identificador único da avaliação (inteiro).
- `description`: descrição da avaliação (texto).
- `nota`: nota dada para o filme (float entre 0.0 e 10.0)
- `id_filme`: identificador do filme avaliado (inteiro)

#### Rotas:

- `GET /avaliacoes`: Retorna a lista de todas as avaliações cadastrados no sistema.
- `GET /avaliacoes/{id_avaliacoes}`: Retorna os detalhes da avaliação com o ID especificado.
- `POST /avaliacoes/adiciona`: Adiciona uma nova avaliação ao sistema.
- `PUT /avaliacoes/{id_avaliacoes}`: Atualiza as informações da avaliação com o ID especificado.
- `DELETE /avaliacoes/{id_avaliacoes}`: Remove a avaliação com o ID especificado do sistema.
- `GET /filmes/{id_filme}/avaliacoes`: Lista todas as avaliações do filme com o ID especificado.
- `GET /filmes/{id_filme}/avaliacoes_media`: Devolve a média das avaliações do filme com o ID especificado.

### Listar toda as Avaliacoes
Rota: `GET /avaliacoes`

Lista todas as avaliações presentes no banco de dados.

Parâmetros:

- Não necessita de parâmetros.

Retorno de exemplo:

```` py
  {
    "id_avaliacao": 0,
    "description": "Filme muito bom",
    "nota": 10,
    "id_filme": 0
  },
  {
    "id_avaliacao": 1,
    "description": "Filme medio",
    "nota": 5,
    "id_filme": 1
  },
  {
    "id_avaliacao": 2,
    "description": "Filme maravilhoso",
    "nota": 8.6,
    "id_filme": 1
  }
]
````

### Listar uma Avaliacao em específico
Rota: `GET /avaliacoes/{id_avaliacoes}`

Lista uma avaliação em específico.

Parâmetros:

- `id_avaliacao` (obrigatório): ID da avaliação que será listado.

Retorno de exemplo:

- Entradas: id_avaliacao = 0

```` py
[
  {
    "id_avaliacao": 0,
    "description": "Filme muito bom",
    "nota": 10,
    "id_filme": 0
  }
]
````

### Adicionar Avaliacao
Rota: `POST /avaliacoes/adiciona`

Adiciona uma nova avaliação ao banco de dados.

Parâmetros:

- `id_filme` (obrigatório): Id do filme avaliado.
- `nota` (obrigatório): Nota do filme avaliado.
- `description` (opcional): Descrição da avaliação a ser adicionado.

Retorno de exemplo:

- Entrada: id_filme = 0; nota = 7.75; description: null.

```` py
[
  {
    "id_avaliacao": 3,
    "description": null,
    "nota": 7.75,
    "id_filme": 0
  }
]
````

- Retorna os dados da avaliação adicionada se a operação for bem-sucedida.

### Atualizar Avaliação
Rota: `PUT /avaliacoes/{id_avaliacoes}`

Atualiza os dados de uma avaliação específico pelo seu ID.

Parâmetros:

- `id_avaliacao` (obrigatório): ID da avaliação a ser atualizado.
- `nota` (opcional): Nova nota para o filme.
- `id_filme` (opcional): Identificador do novo filme.
- `description` (opcional): Nova descrição da avaliação.

Retorno de exemplo:

- Entrada: id_avaliacao = 0; nota = 1.2; id_filme = null; description = Filme muito ruim;

```` py
[
  {
    "id_avaliacao": 0,
    "description": "Filme muito ruim",
    "nota": 1.2,
    "id_filme": 0
  }
]
````

- Retorna os dados da avaliação atualizada se a operação for bem-sucedida.

### Deleta Avaliacao
Rota: `DELETE /avaliacoes/{id_avaliacoes}`

Deleta uma avaliação em específico.

Parâmetros:

- `id_avaliacao` (obrigatório): ID da avaliacao a ser deletada.

Retorno de exemplo:

- Entrada: id_avaliacao = 0.

```` py
[
  {
    "detail": "avaliação deletada"
  }
]
````

- Retorna que a avaliação foi deletada se a operação for bem-sucedida.

### Lista avaliações de um filme específico
Rota: `GET /filmes/{id_filme}/avaliacoes`

Lista todas as avaliações que um filme já recebeu.

Parâmetros:

- `id_filme` (obrigatório): ID do filme a ser atualizado.

Retorno de exemplo:

- Entrada: id_filme = 1.

```` py
[
  {
    "id_avaliacao": 1,
    "description": "Filme medio",
    "nota": 5,
    "id_filme": 1
  },
  {
    "id_avaliacao": 2,
    "description": "Filme maravilhoso",
    "nota": 8.6,
    "id_filme": 1
  }
]
````

### Devolve a avaliação média de um filme específico
Rota: `GET /filmes/{id_filme}/avaliacoes_media`

Lista a média das avaliações que um filme já recebeu.

Parâmetros:

- `id_filme` (obrigatório): ID do filme a ser atualizado.

Retorno de exemplo:

- Entrada: id_filme = 1.

```` py
[
  6.8
]
````

As rotas utilizam a biblioteca pydantic para validar os dados de entrada e de saída da aplicação. Além disso, a aplicação também inclui duas funções auxiliares (`verifica_id_filme` e `verifica_id_avaliacao`) que verificam se um ID de filme ou avaliação existe no banco de dados antes de executar uma operação de busca ou atualização.

Link video: https://youtu.be/iCwl7IdZQj0
