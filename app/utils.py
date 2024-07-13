import aio_pika

from app.client import MailClient
from app.service import MailService
from app.settings import Settings


async def get_mail_service() -> MailService:
    return MailService(
        mail_client=MailClient(settings=Settings())
    )


async def get_amqp_connection() -> aio_pika.abc.AbstractConnection:
    settings = Settings()
    return await aio_pika.connect_robust(settings.AMQP_URL)


async def make_aqmp_consumer():
    mail_service = await get_mail_service()
    connection = await get_amqp_connection()
    channel = await connection.channel()
    queue = await channel.declare_queue("mail_queue", durable=True)
    await queue.consume(mail_service.consume_mail)
