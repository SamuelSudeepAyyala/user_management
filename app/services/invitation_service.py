from uuid import UUID
from app.utils.minio_utils import minio_client
from app.models.invitation_model import Invitation
from app.models.user_model import User  # Assuming the User model exists
from app.database import Database
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import select
from settings.config import Settings
import qrcode
from io import BytesIO
from qrcode.image.pil import PilImage
import base64
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def generate_invitation(inviter_id: UUID, invitee_email: str,db: AsyncSession = Depends(Database.get_session_factory),):
    """
    Generates a unique QR code for the invite, uploads it to MinIO, and saves the invitation to the database.

    Args:
        inviter_id (UUID): The ID of the inviter (user).
        invitee_email (str): The email address of the invitee.
        db (AsyncSession): SQLAlchemy AsyncSession for database interaction.

    Returns:
        dict: Details of the generated invitation including QR code URL.
    """
    try:
        #Fetch the inviter's nickname from the database
        
        async with db() as session:
            result = await session.execute(select(User).where(User.id == inviter_id))
            inviter = result.scalars().first()
        
        if not inviter:
            raise ValueError("Inviter not found in the database.")

        #Encode the inviter's nickname in Base64
        encoded_nickname = base64.urlsafe_b64encode(inviter.nickname.encode()).decode()
        qr_code_url = f"{Settings.Config.APP_BASE_URL}/redirect/?inviter={encoded_nickname}"

        #Generate a QR code with the encoded nickname URL
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white", image_factory=PilImage)

        #Convert the image to bytes for upload
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)

        #Upload the QR code to MinIO
        client = minio_client()
        bucket_name = "qrcodebucket"
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)

        file_name = f"invites/{invitee_email}.png"
        client.put_object(bucket_name, file_name, img_byte_arr, length=img_byte_arr.getbuffer().nbytes)
        qr_code_url = f"http://minio:9000/{bucket_name}/{file_name}"

        #Save the invitation to the database
        invitation = Invitation(
            inviter_id=inviter_id,
            invitee_email=invitee_email,
            qr_code_url=qr_code_url
        )
        async with db() as session:
            session.add(invitation)
            await session.commit()
            await session.refresh(invitation)

        #Log and return the response
        logger.info("Generated and uploaded QR code to MinIO: %s", qr_code_url)
        return {
            "invite_id": str(invitation.id),
            "qr_code_url": invitation.qr_code_url,
            "message": "Invitation successfully generated."
        }

    except Exception as e:
        logger.error("Error generating invitation: %s", e)
        raise ValueError(f"Failed to generate invitation: {str(e)}")
