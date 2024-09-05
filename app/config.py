from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://mongo:27017"
    DATABASE_NAME: str = "clientPortfolioDB"

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]
