from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.invitation_model import Invitation
from app.models.user_model import User
from app.database import Database
from settings.config import Settings
from app.services.invitation_service import generate_invitation
import base64
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter()

# Endpoint: Send Invite
@router.post("/send-invite/")
async def send_invitation(inviter_id: str, invitee_email: str, db: AsyncSession = Depends(Database.get_session_factory)):
    
    try:
        invitation = await generate_invitation(inviter_id, invitee_email, db)
        return {"message": "Invitation sent successfully!", "data": invitation}
    except Exception as e:
        logger.error(f"Failed to send invitation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


# Endpoint: Accept Invite
@router.post("/accept-invite/")
async def accept_invitation(invitee_email: str, db: AsyncSession = Depends(Database.get_session_factory)):
    try:
        # Find pending invitation
        async with db() as session:
            result = await session.execute(
            select(Invitation).where(
                Invitation.invitee_email == invitee_email,
                Invitation.status == "pending"
                )
            )
            invitation = result.scalars().first()

        if not invitation:
            raise HTTPException(status_code=404, detail="Invitation not found or already accepted.")

        # Mark as accepted
        async with db() as session:
            await session.execute(
            update(Invitation)
            .where(Invitation.id == invitation.id)
            .values(status="accepted")
            )
            await session.commit()

        return {"message": "Invitation accepted successfully!"}

    except Exception as e:
        logger.error(f"Failed to accept invitation: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


# Endpoint: Redirect after QR code scan
@router.get("/redirect/")
async def redirect_invitation(inviter: str, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Handles QR code scans, marks the invitation as accepted, and redirects the user.
    """
    try:
        # Decode the inviter nickname from Base64
        decoded_nickname = base64.urlsafe_b64decode(inviter).decode()
        print(decoded_nickname)
        # Find the invitation associated with this nickname
        async with db() as session:
            result = await session.execute(
                select(Invitation).join(User).where(User.nickname == decoded_nickname)
            )
            invitation = result.scalars().first()

        if not invitation:
            raise HTTPException(status_code=404, detail="Invalid invitation or user not found.")

        # Mark invitation as accepted
        async with db() as session:
            if invitation.status != "accepted":
                await session.execute(
                    update(Invitation)
                    .where(Invitation.id == invitation.id)
                    .values(status="accepted")
                )
                await session.commit()

        # Redirect the user to the configured URL
        redirect_url = Settings.Config.BASE_REDIRECT_URL
        return RedirectResponse(url=redirect_url)

    except Exception as e:
        logger.error(f"Failed during QR code redirect: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
