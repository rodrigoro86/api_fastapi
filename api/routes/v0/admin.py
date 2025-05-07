from fastapi import Depends, APIRouter
from api.db.sqlite_connection import get_db_sqlite
from api.db.db_user import UserDB
from api.models.userModel import UserSchema

router = APIRouter()

@router.post("/usuarios")
async def criar_usuario(user: UserSchema, db=Depends(get_db_sqlite)):
    repo = UserDB(db)
    result = await repo.create_user(user)
    return result
