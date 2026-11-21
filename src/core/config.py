from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "DocuAgent AI Engine"
    api_v1_prefix: str = "/api/v1"
    redis_host: str = "localhost"
    redis_port: int = 6379
    similarity_threshold: float = 0.90
    cache_ttl_seconds: int = 3600

    class Config:
        env_file = ".env"

settings = Settings()
