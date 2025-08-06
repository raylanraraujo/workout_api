from typing import Annotated
from pydantic import BaseModel, Field

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='João', max_length=50)]