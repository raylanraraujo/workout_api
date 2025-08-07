from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(str, description='Nome do atleta', examples='João', max_length=50)]
    cpf: Annotated[str, Field(str, description='CPF do atleta', examples='12345678910', max_length=11)]
    idade: Annotated[str, Field(int, description='Idade do atleta', examples=25)]
    nome: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=75.5)]
    nome: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.70)]
    sexo: Annotated[str, Field(str, description='Sexo do atleta', examples='M', max_length=1)]
