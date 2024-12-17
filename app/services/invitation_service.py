from uuid import UUID
from app.utils.minio_utils import minio_client
from app.models.invitation_model import Invitation
from app.database import Database
import qrcode
from io import BytesIO
from qrcode.image.pil import PilImage
from sqlalchemy.ext.asyncio import AsyncSession

async def generate_invitation(inviter_id: UUID, invitee_email: str, db: AsyncSession):
    # Generate a QR Code using Pillow
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"inviter:{inviter_id}, email:{invitee_email}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white", image_factory=PilImage)

    # Convert the image to bytes
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")  # Pillow supports the 'format' argument
    img_byte_arr.seek(0)

    # Save the QR code to Minio
    client = minio_client()
    file_name = f"invites/{invitee_email}.png"
    client.put_object("qrcodebucket", file_name, img_byte_arr, length=img_byte_arr.getbuffer().nbytes)
    qr_code_url = f"http://minio:9000/qrcodebucket/{file_name}"

    # Save invitation to the database
    invitation = Invitation(
        inviter_id=inviter_id,
        invitee_email=invitee_email,
        qr_code_url=qr_code_url
    )
    db.add(invitation)
    await db.commit()
    await db.refresh(invitation)

    return invitation
