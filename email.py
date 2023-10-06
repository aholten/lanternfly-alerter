import boto3
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

region = getenv("REGION")


class EmailContent(BaseModel):
    data: str
    charset: str = "UTF-8"


class EmailSubject(EmailContent):
    pass


class EmailBody(BaseModel):
    text: EmailContent
    html: EmailContent


class EmailMessage(BaseModel):
    subject: EmailSubject
    body: EmailBody


def send_email(source: str, destination: List[str], message: EmailMessage):
    client = boto3.client("ses", region_name=region)

    response = client.send_email(
        Source=source,
        Destination={"ToAddresses": destination},
        Message=message.model_dump(),
    )
    print("Email sent! Message ID:", response["MessageId"])


if __name__ == "__main__":
    message = EmailMessage(
        subject=EmailSubject(data="Hello from SES"),
        body=EmailBody(
            text=EmailContent(data="Hello, this is a test email from AWS SES!"),
            html=EmailContent(
                data="<h1>Hello!</h1><p>This is a test email from AWS SES.</p>"
            ),
        ),
    )

    source = "your_verified_email@example.com"
    destination = ["recipient@example.com"]

    send_email(source, destination, message)
