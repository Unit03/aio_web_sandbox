"""Add 'created_at' column

Revision ID: b9b8abe9c981
Revises: c6e62873fe8d
Create Date: 2016-03-19 21:25:20.549057

"""

# revision identifiers, used by Alembic.
revision = 'b9b8abe9c981'
down_revision = 'c6e62873fe8d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column("bar", sa.Column("created_at", sa.DateTime))


def downgrade():
    op.drop_column("bar", "created_at")
