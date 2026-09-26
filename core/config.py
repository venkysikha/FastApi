# setting up the configuration for the application 

from pydantic_settings import BaseSettings , settingsConfigDict
class Settings(BaseSettings):
    Database_URL: str 
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str ="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    model_config = settingsConfigDict(env_file=".env",extra = "ignore")

settings = Settings()