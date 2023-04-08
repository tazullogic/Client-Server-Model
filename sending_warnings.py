import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email credentials
EMAIL_ADDRESS = "blockchain@maxalogic.com"
EMAIL_PASSWORD = "block123456"


def send_warning_message(user_email):
    # Email subject and body
    subject = 'Warning! Do not use abusing words'
    body = f'Please be respectful with the policy or you will get banned!'

    # Create a message object
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = user_email
    message['Subject'] = subject

    # Add body to message
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and login
    with smtplib.SMTP_SSL('premium97.web-hosting.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send the message
        smtp.send_message(message)

