from fastapi import APIRouter

from api.routes.v0 import endpoint_teste, admin

api_router = APIRouter()

api_router.include_router(endpoint_teste.router, prefix="/teste", tags=["Teste"])
api_router.include_router(admin.router, prefix="/admin", tags=["Administration"])
