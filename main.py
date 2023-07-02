from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/email")
def send_email():
    # Email Sending Code
    return {"success": True, "description": "Email Sent"}


if __name__ == "__main__":
    uvicorn.run(app, port=8001)
