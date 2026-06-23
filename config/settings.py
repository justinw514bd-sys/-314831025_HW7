from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    STORY_API_KEY: str
    STORY_BASE_URL: str
    STORY_MODEL: str

    PROMPT_API_KEY: str
    PROMPT_BASE_URL: str
    PROMPT_MODEL: str

    HF_TOKEN: str

    SD_MODEL: str = (
        "stabilityai/stable-diffusion-xl-base-1.0"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()