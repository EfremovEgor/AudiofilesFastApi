"""init

Revision ID: 49fabf32a2d6
Revises: 
Create Date: 2023-05-22 17:42:47.029394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "49fabf32a2d6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("uuid", sa.UUID(as_uuid=True)),
        sa.Column("username", sa.String, nullable=False),
    )
    op.create_table(
        "audiofiles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("uuid", sa.UUID(as_uuid=True)),
        sa.Column("blob", sa.BLOB, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("audiofiles")
