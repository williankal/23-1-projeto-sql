from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Filmes API",
              description="API para gerenciar filmes e suas avaliações no Multiverso PEDRO ARAGÃO")
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/filmes/adiciona", response_model=schemas.Filme, tags=["Filmes"])
def create_filme(name: str, description: Union[str, None] = None, db: Session = Depends(get_db)):
    """Adiciona um filme ao banco de dados"""
    if "pedro" not in name.lower():
        raise HTTPException(status_code=400, detail="No Multiverso PEDRO ARAGÃO, todos os filmes devem conter o nome 'Pedro'")
    
    return crud.create_filme(db=db, name=name, description=description)


@app.get("/filmes", response_model=list[schemas.Filme], tags=["Filmes"])
def get_filmes(db: Session = Depends(get_db)):
    """Retorna todos os filmes do banco de dados"""
    return crud.get_filmes(db=db)
  
@app.get("/filmes/{id_filme}", response_model=schemas.Filme, tags=["Filmes"])
def get_filme_id(id_filme: int, db: Session = Depends(get_db)):
    """Retorna um filme do banco de dados"""
    db_filme = crud.get_filme(db, id_filme=id_filme)
    if not db_filme:
        raise HTTPException(status_code=400, detail="filme não encontrado")
    return db_filme

@app.put("/filmes/{id_filme}", response_model=schemas.Filme, tags=["Filmes"])
def update_filme(id_filme: int, name:  Union[str, None] = None, description: Union[str, None] = None, db: Session = Depends(get_db)):
    """Atualiza um filme do banco de dados"""
    if not crud.get_filme(db, id_filme=id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")
    
    if name is not None and "pedro" not in name.lower():
        raise HTTPException(status_code=400, detail="No Multiverso PEDRO ARAGÃO, todos os filmes devem conter o nome 'Pedro'")
    
    return crud.update_filme(db=db, id_filme=id_filme, name=name, description=description)
    

@app.delete("/filmes/{id_filme}", tags=["Filmes"])
def delete_filme(id_filme: int, db: Session = Depends(get_db)):
    """Deleta um filme do banco de dados"""
    if not crud.get_filme(db, id_filme=id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")
    
    return crud.delete_filme(db=db, id_filme=id_filme)

@app.get("/filmes/{id_filme}/avaliacoes", tags=["Filmes", "Avaliações"])
def get_avaliacao_do_filme(id_filme: int, db: Session = Depends(get_db)):
    """Retorna todas as avaliações de um filme do banco de dados"""
    if not crud.get_filme(db, id_filme=id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    return crud.get_avaliacao_do_filme(db=db, id_filme=id_filme)
    
@app.get("/filmes/{id_filme}/avaliacoes_media", tags=["Filmes", "Avaliações"])
def get_avaliacao_media_filme(id_filme: int, db: Session = Depends(get_db)):
    """Retorna a média das avaliações de um filme do banco de dado"""
    if not crud.get_filme(db, id_filme=id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    return crud.get_avaliacao_media_filme(db=db, id_filme=id_filme)    

@app.post("/avaliacao/adiciona", response_model=schemas.Avaliacao, tags=["Avaliações"])
def create_avaliacao(id_filme: int, nota: float, description: Union[str,None] = None, db: Session = Depends(get_db)):
    """Adiciona uma avaliação ao banco de dados"""
    if not crud.get_filme(db, id_filme=id_filme):
        raise HTTPException(status_code=404, detail="filme não encontrado")

    return crud.create_avaliacao(db=db, id_filme=id_filme, nota=nota, description=description)
    
    
@app.get("/avaliacoes", tags=["Avaliações"])
def get_avaliacoes(db: Session = Depends(get_db)):
    """Retorna todas as avaliações do banco de dados"""
    return crud.get_avaliacoes(db=db)

@app.get("/avaliacoes/{id_avaliacao}", response_model=schemas.Avaliacao, tags=["Avaliações"])
def get_avaliacao_id(id_avaliacao: int, db: Session = Depends(get_db)):
    """Retorna uma avaliação do banco de dados"""
    db_avali = crud.get_avaliacao(db, id_avaliacao=id_avaliacao)
    if not db_avali:
        raise HTTPException(status_code=400, detail="avaliação não encontrado")
    return db_avali

@app.put("/avaliacao/{id_avaliacao}", tags=["Avaliações"])
def update_avaliacao(id_avaliacao: int, description: Union[str, None] = None, id_filme: Union[int, None] = None, nota: Union[float, None] = None, db: Session = Depends(get_db)):
    """Atualiza uma avaliação do banco de dados"""
    if not crud.get_avaliacao(db, id_avaliacao=id_avaliacao):
        raise HTTPException(status_code=404, detail="avaliação não encontrada")

    if not crud.get_filme(db, id_filme=id_filme) and id_filme is not None:
        raise HTTPException(status_code=404, detail="filme não encontrado")
    
    if nota is not None and (nota < 0 or nota > 10):
        raise HTTPException(status_code=400, detail="nota deve estar entre 0 e 10")

    return crud.update_avaliacao(db=db, id_avaliacao=id_avaliacao, description=description, id_filme=id_filme, nota=nota)

@app.delete("/avaliacao/{id_avaliacao}", tags=["Avaliações"])
def delete_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    """Deleta uma avaliação do banco de dados"""
    if not crud.get_avaliacao(db, id_avaliacao=id_avaliacao):
        raise HTTPException(status_code=404, detail="avaliação não encontrada")

    return crud.delete_avaliacao(db=db, id_avaliacao=id_avaliacao)
