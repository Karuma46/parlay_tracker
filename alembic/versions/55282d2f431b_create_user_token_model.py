"""Create user token model

Revision ID: 55282d2f431b
Revises: 45c7395a4f43
Create Date: 2024-08-15 09:21:32.633602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timedelta

# revision identifiers, used by Alembic.
revision: str = '55282d2f431b'
down_revision: Union[str, None] = '45c7395a4f43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user_tokens',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('token', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, default=datetime.now()),
        sa.Column('expiration', sa.DateTime(), nullable=False, default=datetime.now() + timedelta(days=30)),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('user_tokens')
