from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class InvitationBase(BaseModel):
    inviter_id: UUID
    invitee_email: str
    status: str
    id: UUID
    qr_code_url: str
    created_at: datetime
    updated_at: datetime

class InvitationCreate(InvitationBase):
    pass

class InvitationUpdate(BaseModel):
    status: str

class InvitationRead(InvitationBase):
    
    inviter_id: UUID
    invitee_email: str
    status: str
    id: UUID
    qr_code_url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
        
class PaginationLinks(BaseModel):
    self: str
    next: Optional[str]
    prev: Optional[str]

class PaginatedInvitations(BaseModel):
    data: List[InvitationRead]
    _links: PaginationLinks
