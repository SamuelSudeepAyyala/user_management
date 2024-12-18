from alembic import op
import sqlalchemy as sa
import uuid

revision = "create_invitations_table"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "invitations",
        sa.Column("id", sa.UUID(), primary_key=True, default=uuid.uuid4, index=True),
        sa.Column("inviter_id", sa.UUID(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("invitee_email", sa.String(255), nullable=False),
        sa.Column("nickname", sa.String(100), nullable=False),
        sa.Column("qr_code_url", sa.String(255), nullable=False),
        sa.Column("status", sa.String(20), default="pending", nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    op.drop_table("invitations")
