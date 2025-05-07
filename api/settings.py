import sys
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv(".env", override=True)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )
    API_VERSION: str
    API_NAME: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()
logger.remove()

logger.add(
    Path("logs/app.log"),
    level="INFO",
    retention="20 days",
    rotation="10 MB",
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
    + " | <level>{level: <8}</level> "
    + " | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
    + " - <level>{message}</level>",
)
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
    + " | <level>{level: <8}</level> "
    + " | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
    + " - <level>{message}</level>",
)
