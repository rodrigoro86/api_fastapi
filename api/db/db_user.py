from api.models.userModel import UserSchema


class UserDB:
    def __init__(self, db):  # `db` é a conexão do aiosqlite
        self.db = db

    async def get_user(self, username: str):
        query = """
        SELECT * FROM users
        WHERE username = ?;
        """
        cursor = await self.db.execute(query, (username,))
        row = await cursor.fetchone()
        if row is None:
            return None
        # Exemplo: convertendo para dicionário
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, row))

    async def create_user(self, user: UserSchema):
        query = """
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
        """
        await self.db.execute(query, (user.username, user.email, user.password))
        await self.db.commit()

        # Busca o usuário recém-criado (assumindo que `username` é único)
        return await self.get_user(user.username)
 n  