# @Author  : eco
# @Date    :2025/5/21 21:24
# @Function: 配置管理（通过 pydantic-settings)
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    # APP_NAME: str = "金融数据分析平台"

    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str
    database_url: str

    # 支持从 .env 文件加载配置
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()