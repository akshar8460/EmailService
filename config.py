import os

SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL", "aksharpatel5671@gmail.com")