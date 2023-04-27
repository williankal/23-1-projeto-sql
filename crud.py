from sqlalchemy.orm import Session
from typing import List, Union
import models

def create_filme(db: Session, name: str, description: Union[str, None] = None):   
    db_filme = models.Filme(name=name, description=description)
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def get_filmes(db: Session):
    return db.query(models.Filme).all()

def get_filme(db: Session, id_filme: int):
    return db.query(models.Filme).filter(models.Filme.id_filme == id_filme).first()

def update_filme(db: Session, id_filme: int, name:  Union[str, None] = None, description: Union[str, None] = None):
    db_filme = get_filme(db, id_filme=id_filme)
    if name:
        db_filme.name = name
    if description:
        db_filme.description = description
    db.commit()
    db.refresh(db_filme)
    return db_filme

def delete_filme(db: Session, id_filme: int):
    db_filme = get_filme(db, id_filme=id_filme)
    db.delete(db_filme)
    db.commit()
    return db_filme

def get_avaliacao_do_filme(db: Session, id_filme: int):
    return db.query(models.Avaliacao).filter(models.Avaliacao.id_filme == id_filme).all()

def get_avaliacao_media_filme(db: Session, id_filme: int):
    ava_media = get_avaliacao_do_filme(db, id_filme=id_filme)
    soma = 0
    for i in ava_media:
        soma += i.nota
    return round(soma/len(ava_media), 2)

def create_avaliacao(db: Session, id_filme: int, description: Union[str, None] = None, nota: float = 0.0):
    db_avaliacao = models.Avaliacao(description=description, nota=nota, id_filme=id_filme)
    db.add(db_avaliacao)
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

def get_avaliacoes(db: Session):
    return db.query(models.Avaliacao).all()

def get_avaliacao(db: Session, id_avaliacao: int):
    return db.query(models.Avaliacao).filter(models.Avaliacao.id_avaliacao == id_avaliacao).first()

def update_avaliacao(db: Session, id_avaliacao: int, description: Union[str, None] = None, id_filme: Union[int, None] = None, nota: Union[float, None] = None):
    db_avaliacao = get_avaliacao(db, id_avaliacao=id_avaliacao)
    if description:
        db_avaliacao.description = description
    if id_filme:
        db_avaliacao.id_filme = id_filme
    if nota:
        db_avaliacao.nota = nota
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

def delete_avaliacao(db: Session, id_avaliacao: int):
    db_avaliacao = get_avaliacao(db, id_avaliacao=id_avaliacao)
    db.delete(db_avaliacao)
    db.commit()
    return db_avaliacao