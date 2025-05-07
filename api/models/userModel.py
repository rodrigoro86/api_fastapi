from typing import Dict, Optional

from pydantic import BaseModel, EmailStr, Field


class Message(BaseModel):
    message: str


class UserPasswordSchema(BaseModel):
    new_password: str


class UserSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]


class LogModel(BaseModel):
    username: str = Field(..., description="Nome do usuário")
    endpoint: str = Field(..., description="Endpoint acessado")
    status: str = Field(..., description="Status da requisição")
    params: Dict = Field(
        ..., description="Parâmetros passados para o endpoint"
    )
    results: Dict = Field(..., description="Resultados da requisição")


class UserUpdateResponse(BaseModel):
    message: str = Field(
        "Usuário atualizado com sucesso!", description="Mensagem de sucesso"
    )
