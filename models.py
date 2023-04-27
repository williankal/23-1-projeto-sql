from sqlalchemy import Column, ForeignKey, Integer, String, Float

from database import Base


class Filme(Base):
    __tablename__ = "filmes"

    id_filme = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(80))
    description = Column(String(80), nullable=True)


class Avaliacao(Base):
    __tablename__ = "Avaliacao"

    id_avaliacao = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    description = Column(String(80))
    nota = Column(Float) 

    id_filme = Column(ForeignKey("filmes.id_filme"))