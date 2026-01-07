import os


class settings():
    JWT_SECRET :str  = os.getenv("SECRET_KEY", "change_in_production")
    JWT_ALG: str ="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    API_V1_STR: str = "/api/v1"

settings = settings()