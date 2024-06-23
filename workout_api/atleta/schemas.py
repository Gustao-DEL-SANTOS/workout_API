from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat


class Atleta(BaseModel):
    nome: Annotated[
        str, Field(description="NOME do atleta", examples="Joao", max_length=50)
    ]
    cpf: Annotated[str, Field(description="CPF do atleta", examples="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="IDADE do atleta", examples="25")]
    peso: Annotated[PositiveFloat, Field(description="PESO do atleta", examples="75.5")]
    altura: Annotated[PositiveFloat, Field(description="ALTURA do atleta", examples="1.69")]
    sexo: Annotated[str, Field(description="SEXO do atleta", examples="M", max_length=1)]
