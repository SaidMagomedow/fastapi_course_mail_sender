import smtplib
import ssl
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.settings import Settings

@dataclass
class MailClient:
    settings: Settings

    def send_email_task(self, subject: str, text: str, to: str):
        msg = self._build_message(subject, text, to)
        self._send_email(msg=msg)

    def _build_message(self, subject: str, text: str, to: str) -> MIMEMultipart:
        msg = MIMEMultipart()

        msg["From"] = self.settings.from_email
        msg["To"] = to
        msg["Subject"] = subject
        msg.attach(MIMEText(text, "plain"))
        return msg

    def _send_email(self, msg: MIMEMultipart):
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(self.settings.SMTP_HOST, self.settings.SMTP_PORT, context=context)
        server.login(self.settings.from_email, self.settings.SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
