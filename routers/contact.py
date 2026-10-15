from fastapi import APIRouter, Request, HTTPException
from models.schemas import ContactRequest
from services.email_service import send_email

from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()

limiter = Limiter(key_func=get_remote_address)


@router.post("/contact")
@limiter.limit("5/hour")
async def contact(
    request: Request,
    payload: ContactRequest
):

    try:

        send_email(
            name=payload.name,
            email=payload.email,
            message=payload.message
        )

        return {
            "success": True,
            "message": "Message sent!"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )