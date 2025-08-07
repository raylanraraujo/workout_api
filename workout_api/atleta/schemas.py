from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(str, description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(str, description='CPF do atleta', example='12345678910', max_length=11)]
    idade: Annotated[str, Field(int, description='Idade do atleta', example=25)]
    nome: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    nome: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(str, description='Sexo do atleta', example='M', max_length=1)]
    