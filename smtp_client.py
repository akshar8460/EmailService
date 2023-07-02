import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import *

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('email_template.html')


def send_email(sender_email, receiver_email, subject, name, info):
    # SMTP server configuration
    smtp_port = 587

    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # HTML Content
    context = {
        "name": name,
        "info": info
    }
    html_content = template.render(context)

    # Add message body
    # msg.attach(MIMEText(message, "plain"))

    # Attach the HTML content
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Create a SMTP session
        with smtplib.SMTP(SMTP_SERVER, smtp_port) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            # Send email
            server.send_message(msg)
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))


# Example usage
sender_email = "aksharpatel5671@gmail.com"
receiver_email = "akshar8460@gmail.com"
subject = "Test Email"
# message = "This is a test email sent from Python."

send_email(sender_email, receiver_email, subject, name="Ganesh", info="Temporary Information..!!")
