from typing import Annotated, Optional

from pydantic import BaseModel, Field, PositiveFloat

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamento
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseModel):
    nome: Annotated[str, Field(description="NOME do atleta", example="Joao", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900",max_length=11)]
    idade: Annotated[int, Field(description="IDADE do atleta", example="25")]
    peso: Annotated[PositiveFloat, Field(description="PESO do atleta", example="75.5")]
    altura: Annotated[PositiveFloat, Field(description="ALTURA do atleta", example="1.69")]
    sexo: Annotated[str, Field(description="SEXO do atleta", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamento, Field(description="CentroTreinamento do atleta")]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="NOME do atleta", example="Joao", max_length=50)]
    cpf: Annotated[Optional[str], Field(None, description="CPF do atleta", example="12345678900",max_length=11)]
    idade: Annotated[Optional[int], Field(None, description="IDADE do atleta", example="25")]
    