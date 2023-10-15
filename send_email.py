import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  

PORT = 587  
EMAIL_SERVER = "smtp.gmail.com"  

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name, due_date, amount):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Syren0914.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi <strong> {name} </strong>,
        I hope you are well.
        I just wanted to drop you a quick note to remind you that tomorrow is PAD DAYYY {amount} USD.
        Thank you for using our service. :D
        Best regards
        Syren0914
        """
    )
    
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that tomorrow is PAD DAYYY   <strong>{amount} USD</strong>.
        <p> Thank you for using our service. :D</p>
        <p></p>

        <p>Best regards</p>
        <p>Syren0914</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

