import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import *

from jinja2 import Environment, FileSystemLoader

from email_mapping import EMAIL_MAPPER

env = Environment(loader=FileSystemLoader('templates'))


def send_email(receiver_email, email_type, template_data):
    # SMTP server configuration
    smtp_port = 587

    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = EMAIL_MAPPER.get(email_type)

    # HTML Content
    template = env.get_template(f'{email_type}.html')
    html_content = template.render(template_data)

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
if __name__ == "__main__":
    sender_email = "aksharpatel5671@gmail.com"
    receiver_email = "akshar8460@gmail.com"
    subject = "Test Email"
    # message = "This is a test email sent from Python."

    send_email(sender_email, receiver_email, subject)
