"""Create bar table

Revision ID: c6e62873fe8d
Revises:
Create Date: 2016-03-19 20:54:39.612653

"""

# revision identifiers, used by Alembic.
revision = 'c6e62873fe8d'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "bar",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table("bar")
