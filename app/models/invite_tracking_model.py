import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

class InviteStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"

class InviteTracking(Base):
    __tablename__ = "invite_tracking"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    inviter_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    invitee_email: Mapped[str] = mapped_column(String(255), nullable=False)
    qr_code_url: Mapped[str] = mapped_column(String(500), nullable=False)
    status: Mapped[InviteStatus] = mapped_column(Enum(InviteStatus, name="invite_status_enum"), default=InviteStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    inviter = relationship("User", back_populates="invites")
