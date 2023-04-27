from typing import List, Optional

from pydantic import BaseModel, Field

class FilmeBase(BaseModel):
    name: str = Field(
        title="Nome do filme",
        description="Nome do filme",
    )
    
    description: str | None = Field(
        title="Descrição do filme",
        description="Descrição do filme",
        default=None,
    )

class FilmeCreate(FilmeBase):
    pass

class Filme(FilmeBase):
    """Modelo de filme"""

    id_filme: int = Field(
        title="ID do filme",
        description="ID do filme",
        ge=0,
    )
    class Config:
        orm_mode = True


class AvaliacaoBase(BaseModel):
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

class AvaliacaoCreate(AvaliacaoBase):
    pass

class Avaliacao(AvaliacaoBase):
    """Modelo de avaliação"""

    id_avaliacao: int = Field(
        title="ID da avaliação",
        description="ID da avaliação",
        ge=0,
    )

    id_filme: int = Field(
        title="ID extrangeiro do filme",
        description="ID extrangeiro do filme",
        ge=0,
    )
    
    class Config:
        orm_mode = True


