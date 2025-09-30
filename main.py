from fastapi import FastAPI
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError

app = FastAPI(title="Email Validation API", description="API simple pour valider des emails", version="1.0")

class EmailRequest(BaseModel):
    email: str

@app.post("/validate-email/")
async def validate_email_api(request: EmailRequest):
    try:
        valid = validate_email(request.email)
        return {
            "email": request.email,
            "valid": True,
            "normalized": valid.email,
            "domain": valid.domain
        }
    except EmailNotValidError as e:
        return {
            "email": request.email,
            "valid": False,
            "error": str(e)
        }

