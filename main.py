import uvicorn
from fastapi import FastAPI
from schema import *
import smtp_client
app = FastAPI()


@app.post("/email")
def send_email(payload: SendEmail):
    rec_email = payload.email
    email_type = payload.type
    template_data = payload.template_data
    smtp_client.send_email(rec_email, email_type, template_data)
    return {"success": True, "description": "Email Sent"}


if __name__ == "__main__":
    uvicorn.run(app, port=8001)
