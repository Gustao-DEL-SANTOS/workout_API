from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str,Field(description="NOME do centro de treinamento",example="CT King",max_length=20)]
    endereco: Annotated[str,Field(description="Endereco do centro de treinamento",example="Rua Del JHK 2",max_length=60)]
    proprietario: Annotated[str,Field(description="Nome do proprietario",example="Cidao",max_length=30)]
