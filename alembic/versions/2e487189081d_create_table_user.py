"""create_table_user

Revision ID: 2e487189081d
Revises: 
Create Date: 2024-05-19 19:14:02.035670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e487189081d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('cellphone', sa.String(30), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('hash', sa.String(150), nullable=False),
        sa.Column('birth_date', sa.DateTime, nullable=True),
        sa.Column('address', sa.String(100), nullable=True),
        sa.Column('zip_code', sa.String(50), nullable=True),
        sa.Column('number', sa.String(10), nullable=True),
        sa.Column('role', sa.Enum('admin', 'user', 'employee'), nullable=False),
    )    


def downgrade() -> None:
    op.drop_table('users')
