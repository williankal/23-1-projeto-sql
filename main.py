from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from statistics import mean

app = FastAPI(title="Filmes API",
              description="API para gerenciar filmes e suas avaliações no Multiverso PEDRO ARAGÃO")

class Filme(BaseModel):
    """Modelo de filme"""

    id_filme: int = Field(
        title="ID do filme",
        description="ID do filme",
        ge=0,
    )

    name: str = Field(
        title="Nome do filme",
        description="Nome do filme",
    )

    description: str | None = Field(
        title="Descrição do filme",
        description="Descrição do filme",
        default=None,
    )


class Avaliacao(BaseModel):
    """Modelo de avaliação"""

    id_avaliacao: int = Field(
        title="ID da avaliação",
        description="ID da avaliação",
        ge=0,
    )

    description: str | None = Field(
        title="Descrição da avaliação",
        description="Descrição da avaliação",
        default=None,
    )

    nota: float = Field(
        title="Nota do filme",
        description="Nota do filme",
        ge=0.0,
        le=10.0,
    )

    id_filme: int = Field(
        title="ID extrangeiro do filme",
        description="ID extrangeiro do filme",
        ge=0,
    )


banco = {
    "filmes": [
        Filme(id_filme=0, name="Pedro Aragão", description="Filme sobre o Pedro Aragão"),
        Filme(id_filme=1, name="Pedro Aragão 2", description="Filme sobre o Pedro Aragão 2"),
        Filme(id_filme=2, name="Pedro Aragão 3", description="Filme sobre o Pedro Aragão 3"),
    ],
    "avaliacoes": [
        Avaliacao(id_avaliacao=0, description="Filme muito bom", nota=10.0, id_filme=0),
        Avaliacao(id_avaliacao=1, description="Filme medio", nota=5.0, id_filme=1),
        Avaliacao(id_avaliacao=2, description="Filme maravilhoso", nota=8.6, id_filme=1),
    ]
}

def verifica_id_filme(id_filme: int):
    """Verifica se o id_filme existe no banco de dados"""
    if len([i for i in range(len(banco["filmes"])) if banco["filmes"][i].id_filme == id_filme]) == 0:
        return True
    return False

def verifica_id_avaliacao(id_avaliacao: int):
    """Verifica se o id_avaliacao existe no banco de dados"""
    if len([i for i in range(len(banco["avaliacoes"])) if banco["avaliacoes"][i].id_avaliacao == id_avaliacao]) == 0:
        return True
    return False

@app.post("/filmes/adiciona", tags=["Filmes"])
def create_filme(name: str, description: Union[str, None] = None):
    """Adiciona um filme ao banco de dados"""
    try:
        if "pedro" not in name.lower():
            return {"detail":"Nome do filme inválido, no multiverso Pedro não existe filmes sem ele"}
        
        filme_create = Filme(name=name, description=description, id_filme = banco["filmes"][-1].id_filme + 1 if len(banco["filmes"]) >= 1 else 0)
        banco["filmes"].append(filme_create)
        return banco["filmes"][-1]
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    

@app.get("/filmes", tags=["Filmes"])
def get_filmes():
    """Retorna todos os filmes do banco de dados"""
    try:
        return banco["filmes"]
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    
  
@app.get("/filmes/{id_filme}", tags=["Filmes"])
def get_filme_id(id_filme: int):
    """Retorna um filme do banco de dados"""
    if verifica_id_filme(id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    try:
        return banco["filmes"][id_filme]
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    

@app.put("/filmes/{id_filme}", tags=["Filmes"])
def update_filme(id_filme: int, name:  Union[str, None] = None, description: Union[str, None] = None):
    """Atualiza um filme do banco de dados"""
    if verifica_id_filme(id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")
    try:
        if name is not None and "pedro" not in name.lower():
            return {"detail":"Nome do filme inválido, no multiverso Pedro não existe filmes sem ele"}
        
        print([i for i in range(len(banco["filmes"])) if banco["filmes"][i].id_filme==id_filme][0])
        encontra_id = [i for i in range(len(banco["filmes"])) if banco["filmes"][i].id_filme==id_filme][0]
        print(encontra_id)
        if description is not None:
            banco["filmes"][encontra_id].description = description
        if name is not None:
            banco["filmes"][encontra_id].name = name
        return banco["filmes"][encontra_id]
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    

@app.delete("/filmes/{id_filme}", tags=["Filmes"])
def delete_filme(id_filme: int):
    """Deleta um filme do banco de dados"""
    print(verifica_id_filme(id_filme))
    if verifica_id_filme(id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    try:
        # exclui o filme do banco de dados
        banco["filmes"].pop([i for i in range(len(banco["filmes"])) if banco["filmes"][i].id_filme==id_filme][0])

        lista_avaliacoes = [i for i in banco["avaliacoes"] if i.id_filme == id_filme]

        for avaliacao in lista_avaliacoes:
            if avaliacao.id_filme == id_filme:
                banco["avaliacoes"].remove(avaliacao)
                        
        return {"detail": "filme deletado"}
    except:
        raise HTTPException(status_code=500, detail="erro interno")


@app.get("/filmes/{id_filme}/avaliacoes", tags=["Filmes", "Avaliações"])
def get_avaliacao_do_filme(id_filme: int):
    """Retorna todas as avaliações de um filme do banco de dados"""
    if verifica_id_filme(id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    try:
        aval = []
        for avaliacao in banco["avaliacoes"]:
            if avaliacao.id_filme == id_filme:
                aval.append(avaliacao)

        return aval
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    
@app.get("/filmes/{id_filme}/avaliacoes_media", tags=["Filmes", "Avaliações"])
def get_avaliacao_media_filme(id_filme: int):
    """Retorna a média das avaliações de um filme do banco de dado"""
    if verifica_id_filme(id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    try:
        aval = []
        for avaliacao in banco["avaliacoes"]:
            if avaliacao.id_filme == id_filme:
                aval.append(avaliacao.nota)
        if not aval:
            return {"detail":"filme não possui avaliações"}

        return mean(aval)
    
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    

@app.post("/avaliacao/adiciona", tags=["Avaliações"])
def create_avaliacao(id_filme: int, nota: float, description: Union[str,None] = None):
    """Adiciona uma avaliação ao banco de dados"""
    if verifica_id_filme(id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")
    
    if nota < 0 or nota > 10:
        raise HTTPException(status_code=400, detail="nota fora do intervalo (0, 10)")

    try:
        avaliacao_create = Avaliacao(description=description, id_filme=id_filme, nota=nota, id_avaliacao = banco["avaliacoes"][-1].id_avaliacao + 1 if len(banco["avaliacoes"]) >= 1 else 0)
        banco["avaliacoes"].append(avaliacao_create)
        return banco["avaliacoes"][-1]
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    
    
@app.get("/avaliacoes", tags=["Avaliações"])
def get_avaliacoes():
    """Retorna todas as avaliações do banco de dados"""
    try:
        return banco["avaliacoes"]
    except:
        raise HTTPException(status_code=500, detail="erro interno")
    

@app.get("/avaliacoes/{id_avaliacao}", tags=["Avaliações"])
def get_avaliacao_id(id_avaliacao: int):
    """Retorna uma avaliação do banco de dados"""
    if verifica_id_avaliacao(id_avaliacao):
        raise HTTPException(status_code=404, detail="avaliação não encontrada")
    
    try:
        return banco["avaliacoes"][id_avaliacao]
    except:
        raise HTTPException(status_code=500, detail="erro interno")


@app.delete("/avaliacao/{id_avaliacao}", tags=["Avaliações"])
def delete_avaliacao(id_avaliacao: int):
    """Deleta uma avaliação do banco de dados"""
    if verifica_id_avaliacao(id_avaliacao):
        raise HTTPException(status_code=404, detail="avaliação não encontrada")

    try:
        banco["avaliacoes"].pop([i for i in range(len(banco["avaliacoes"])) if banco["avaliacoes"][i].id_avaliacao==id_avaliacao][0])
        return {"detail": "avaliação deletada"}
    except:
        raise HTTPException(status_code=500, detail="erro interno")


@app.put("/avaliacao/{id_avaliacao}", tags=["Avaliações"])
def update_avaliacao(id_avaliacao: int, description: Union[str, None] = None, id_filme: Union[int, None] = None, nota: Union[float, None] = None):
    """Atualiza uma avaliação do banco de dados"""
    if verifica_id_avaliacao(id_avaliacao):
        raise HTTPException(status_code=404, detail="avaliação não encontrada")
    
    if verifica_id_filme(id_filme) and id_filme is not None:
        raise HTTPException(status_code=404, detail="filme não encontrado")
    
    if (nota is not None):
        if nota < 0 or nota > 10:
            raise HTTPException(status_code=400, detail="nota fora do intervalo (0, 10)")

    try:
        encontra_id = [i for i in range(len(banco["avaliacoes"])) if banco["avaliacoes"][i].id_avaliacao==id_avaliacao][0]
        if description is not None:
            banco["avaliacoes"][encontra_id].description = description
        if id_filme is not None:
            banco["avaliacoes"][encontra_id].id_filme = id_filme
        if nota is not None:
            banco["avaliacoes"][encontra_id].nota = nota

        return banco["avaliacoes"][encontra_id]
    
    except:
        raise HTTPException(status_code=500, detail="erro interno")
