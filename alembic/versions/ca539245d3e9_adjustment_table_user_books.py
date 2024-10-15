"""Ajuste tabela users_books

Revision ID: ca539245d3e9
Revises: fc0cc738a5f1
Create Date: 2024-10-15 19:04:15.419350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca539245d3e9'
down_revision: Union[str, None] = 'fc0cc738a5f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('users_books')

    op.create_table(
        'users_books',
        sa.Column('id_user', sa.Integer(), nullable=False),
        sa.Column('id_book', sa.Integer(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('users_books')
