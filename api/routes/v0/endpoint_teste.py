from fastapi import APIRouter
from http import HTTPStatus
from api.models.testeModel import TesteResponseModel

router = APIRouter()


@router.get(
    "/teste/",
    status_code=HTTPStatus.OK,
    response_model=TesteResponseModel,
    summary="Endepoint de Teste",
    description="Este endpoint valida se a API está funcionando",
    responses={
        HTTPStatus.UNAUTHORIZED: {
            "description": "Token expirado ou inválido.",
            "content": {
                "application/json": {"example": {"detail": "Token expirado."}}
            },
        },
    },
)
async def teste_endpoint():

    return TesteResponseModel(message = 'Teste')
