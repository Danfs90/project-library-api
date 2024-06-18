"""create_table_user_books

Revision ID: fc0cc738a5f1
Revises: 240d851a4cca
Create Date: 2024-06-18 20:23:24.911546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc0cc738a5f1'
down_revision: Union[str, None] = '240d851a4cca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Criação da tabela de associação com chaves estrangeiras
    op.create_table(
        'users_books',
        sa.Column('id_user', sa.Integer, sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('id_book', sa.Integer, sa.ForeignKey('books.id'), primary_key=True),
    )

def downgrade():
    # Exclusão da tabela de associação
    op.drop_table('users_books')