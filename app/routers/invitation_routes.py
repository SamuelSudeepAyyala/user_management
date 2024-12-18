from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends, Query
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
from sqlalchemy import func
from app.schemas.invitations_schema import InvitationRead,InvitationCreate,InvitationBase,InvitationUpdate, PaginatedInvitations

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

@router.get("/invitation-stats/")
async def get_invitation_stats(user_id: UUID, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Returns the number of invitations sent and accepted by a user.
    
    Args:
        user_id (UUID): The ID of the user.
        db (AsyncSession): The database session dependency.

    Returns:
        JSON object with invitation stats.
    """
    try:
        # Total invites sent by the user
        async with db() as session:
            total_invites_query = await session.execute(
                select(func.count(Invitation.id)).filter(Invitation.inviter_id == user_id)
            )
            total_invites = total_invites_query.scalar() or 0

        # Total invites accepted
            accepted_invites_query = await session.execute(
                select(func.count(Invitation.id)).filter(
                    Invitation.inviter_id == user_id,
                    Invitation.status == "accepted"
                )
            )
            accepted_invites = accepted_invites_query.scalar() or 0

        return {
            "user_id": str(user_id),
            "total_invites_sent": total_invites,
            "total_invites_accepted": accepted_invites
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching stats: {str(e)}")
    
## Implementing BREAD HATEOS Endpoints

#Browse Endpoint
@router.get("/get_invitations/", response_model=PaginatedInvitations)
async def get_invitations(page: int = Query(1, ge=1),size: int = Query(10, ge=1),db: AsyncSession = Depends(Database.get_session_factory)):
    try:
        offset = (page - 1) * size
        query = select(Invitation).offset(offset).limit(size)
        async with db() as session:
            result = await session.execute(query)
            invitations = result.scalars().all()

        # Pagination links
        base_url = f"/invitations/?page={page}&size={size}"
        next_page = f"/invitations/?page={page + 1}&size={size}"
        prev_page = f"/invitations/?page={max(1, page - 1)}&size={size}"
        response = {
            "data": invitations,
            "_links": {
                "self": base_url,
                "next": next_page if len(invitations) == size else None,
                "prev": prev_page if page > 1 else None
            }
        }

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching invitations: {str(e)}")

#Read Endpoint
@router.get("/read_invitations/", response_model=InvitationRead)
async def read_invitation(user_id: UUID, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Retrieve a specific invitation by ID.
    """
    try:
        async with db() as session:
            
            result = await session.execute(select(Invitation).where(Invitation.inviter_id == user_id))
            invitation = result.scalars().first()

        if not invitation:
            raise HTTPException(status_code=404, detail="Invitation not found.")
        
        return InvitationRead.from_orm(invitation)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading invitation: {str(e)}")

#Edit Endpoint
@router.put("/edit_invitations/{invitation_id}", response_model=InvitationRead)
async def edit_invitation(invitation_id: UUID, invitation_data: InvitationUpdate, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Update invitation details.
    """
    try:
        async with db() as session:
            result = await session.execute(select(Invitation).where(Invitation.id == invitation_id))
            invitation = result.scalar()

            if not invitation:
                raise HTTPException(status_code=404, detail="Invitation not found.")

            # Update invitation fields
            for field, value in invitation_data.dict(exclude_unset=True).items():
                setattr(invitation, field, value)
            
            await session.commit()
            await session.refresh(invitation)

        return invitation
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating invitation: {str(e)}")

#Add Endpoint
@router.post("/add_invitations/", response_model=InvitationRead)
async def add_invitation(invitation_data: InvitationCreate, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Create a new invitation.
    """
    try:
        async with db() as session:
            invitation = Invitation(**invitation_data.dict())
            session.add(invitation)
            await session.commit()
            await session.refresh(invitation)

        return invitation
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating invitation: {str(e)}")

#Delete Endpoint
@router.delete("/delete_invitations/{invitation_id}", response_model=dict)
async def delete_invitation(invitation_id: UUID, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Delete an invitation by ID.
    """
    try:
        async with db() as session:
            result = await session.execute(select(Invitation).where(Invitation.id == invitation_id))
            invitation = result.scalar()

        if not invitation:
            raise HTTPException(status_code=404, detail="Invitation not found.")
        
        async with db() as session:
            await session.delete(invitation)
            await session.commit()

        return {
            "message" : "Invitation Deleted Successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting invitation: {str(e)}")
