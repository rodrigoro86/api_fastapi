from typing import AsyncGenerator
import aiosqlite
from pathlib import Path

from api.settings import Settings, logger


DB_PATH = Path("data/db_api.sqlite")
sqlite_conn = None

async def init_sqlite_conn():
    """Inicializa conexão global SQLite ao iniciar a API."""
    global sqlite_conn
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)  # <-- Cria pasta se não existir
        sqlite_conn = await aiosqlite.connect(DB_PATH)
        await sqlite_conn.execute("PRAGMA foreign_keys = ON;")
        logger.info("✅ Conexão com SQLite inicializada")
    except Exception as e:
        logger.error(f"❌ Erro ao conectar no SQLite: {e}")
        raise RuntimeError(f"Erro ao conectar no SQLite: {e}")


async def close_sqlite_conn():
    """Fecha a conexão SQLite ao desligar a API."""
    global sqlite_conn
    if sqlite_conn:
        await sqlite_conn.close()
        logger.info("🛑 Conexão com SQLite encerrada")


async def get_db_sqlite() -> AsyncGenerator[aiosqlite.Connection, None]:
    """Obtém a conexão global SQLite para uso em endpoints."""
    global sqlite_conn
    if sqlite_conn is None:
        raise RuntimeError("🔴 A conexão SQLite ainda não foi inicializada!")

    try:
        yield sqlite_conn
    finally:
        pass  # Conexão não é liberada aqui pois é gerenciada globalmente
