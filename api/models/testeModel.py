from pydantic import BaseModel, Field


class TesteResponseModel(BaseModel):
    message: str = Field(..., description="Resposta OK!!!")
