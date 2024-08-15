"""Add tokens to user model

Revision ID: af0546e2f506
Revises: 55282d2f431b
Create Date: 2024-08-15 09:43:33.976226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af0546e2f506'
down_revision: Union[str, None] = '55282d2f431b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('tokens', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'tokens')
