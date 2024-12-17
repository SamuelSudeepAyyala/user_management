from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Invitation(Base):
    __tablename__ = "invitations"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid4)
    inviter_id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    invitee_email: Mapped[str] = Column(String(255), nullable=False, index=True)
    qr_code_url: Mapped[str] = Column(String(500), nullable=False)
    accepted: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Import User model after 'Base' and define the relationship

    inviter: Mapped["User"] = relationship("User", back_populates="invitations_sent")
