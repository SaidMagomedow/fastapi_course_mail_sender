from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    from_email: str = "no-reply@fitra.live"
    SMTP_PORT: int = 465
    SMTP_HOST: str = "smtp.yandex.ru"
    SMTP_PASSWORD: str = ""
    AMQP_URL: str = 'amqp://guest:guest@localhost:5672//'
