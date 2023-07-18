from pydantic import BaseModel, EmailStr


class SendEmail(BaseModel):
    email: EmailStr
    type: str
    template_data: dict
