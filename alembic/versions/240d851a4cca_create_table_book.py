"""create_table_book

Revision ID: 240d851a4cca
Revises: 2e487189081d
Create Date: 2024-06-09 22:24:21.715260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '240d851a4cca'
down_revision: Union[str, None] = '2e487189081d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('author', sa.String(length=255), nullable=False),
        sa.Column('publication_date', sa.Date, nullable=False),
        sa.Column('isbn', sa.String(length=20), nullable=True),
        sa.Column('publisher', sa.String(length=255), nullable=False),
        sa.Column('genre', sa.String(length=50), nullable=False),
        sa.Column('page_count', sa.Integer, nullable=False),
        sa.Column('language', sa.String(length=50), nullable=False),
        sa.Column('summary', sa.Text, nullable=True),
        sa.Column('cover_image', sa.String(length=255), nullable=True),
        sa.Column('stock', sa.Integer, nullable=False),
        sa.Column('price', sa.Numeric(10, 2), nullable=False)
    )

    # Inserção dos dados
    op.bulk_insert(
        sa.table('books',
                 sa.column('title', sa.String),
                 sa.column('author', sa.String),
                 sa.column('publication_date', sa.Date),
                 sa.column('isbn', sa.String),
                 sa.column('publisher', sa.String),
                 sa.column('genre', sa.String),
                 sa.column('page_count', sa.Integer),
                 sa.column('language', sa.String),
                 sa.column('summary', sa.Text),
                 sa.column('cover_image', sa.String),
                 sa.column('stock', sa.Integer),
                 sa.column('price', sa.Numeric)
                 ),
        [
            {'title': 'A Dança dos Dragões', 'author': 'George R. R. Martin', 'publication_date': '2011-07-12', 'isbn': '9780553801477', 'publisher': 'Bantam Books', 'genre': 'Fantasia', 'page_count': 1056, 'language': 'Inglês', 'summary': 'Quinto livro da série de fantasia épica "As Crônicas de Gelo e Fogo".', 'cover_image': 'link_to_cover_image_11.jpg', 'stock': 10, 'price': 15.99},
            {'title': 'Harry Potter e as Relíquias da Morte', 'author': 'J.K. Rowling', 'publication_date': '2007-07-21', 'isbn': '9780545010221', 'publisher': 'Bloomsbury Publishing', 'genre': 'Fantasia', 'page_count': 759, 'language': 'Inglês', 'summary': 'O sétimo e último livro da série "Harry Potter", que culmina na batalha final entre Harry e Lord Voldemort.', 'cover_image': 'link_to_cover_image_13.jpg', 'stock': 15, 'price': 14.99},
            {'title': 'A Culpa é das Estrelas', 'author': 'John Green', 'publication_date': '2012-01-10', 'isbn': '9781594137907', 'publisher': 'Dutton Books', 'genre': 'Ficção Adolescente', 'page_count': 313, 'language': 'Inglês', 'summary': 'Um romance sobre dois adolescentes que se conhecem em um grupo de apoio para pacientes com câncer.', 'cover_image': 'link_to_cover_image_14.jpg', 'stock': 20, 'price': 9.99},
            {'title': 'O Orfanato da Srta. Peregrine Para Crianças Peculiares', 'author': 'Ransom Riggs', 'publication_date': '2011-06-07', 'isbn': '9781594137907', 'publisher': 'Quirk Books', 'genre': 'Fantasia', 'page_count': 382, 'language': 'Inglês', 'summary': 'O primeiro livro da trilogia, uma mistura de romance e horror gótico.', 'cover_image': 'link_to_cover_image_15.jpg', 'stock': 12, 'price': 11.00},
            {'title': 'Cidade dos Ossos', 'author': 'Cassandra Clare', 'publication_date': '2007-03-27', 'isbn': '9781416955078', 'publisher': 'Margaret K. McElderry Books', 'genre': 'Fantasia Urbana', 'page_count': 485, 'language': 'Inglês', 'summary': 'O primeiro livro da série "Os Instrumentos Mortais", que segue a jornada de Clary Fray no mundo dos Caçadores de Sombras.', 'cover_image': 'link_to_cover_image_16.jpg', 'stock': 18, 'price': 10.25},
            {'title': 'Divergente', 'author': 'Veronica Roth', 'publication_date': '2011-05-03', 'isbn': '9780062387240', 'publisher': 'Katherine Tegen Books', 'genre': 'Distopia', 'page_count': 487, 'language': 'Inglês', 'summary': 'O primeiro livro da trilogia "Divergente", que se passa em uma sociedade futurista dividida em facções.', 'cover_image': 'link_to_cover_image_17.jpg', 'stock': 11, 'price': 9.75},
            {'title': 'Jogos Vorazes', 'author': 'Suzanne Collins', 'publication_date': '2008-09-14', 'isbn': '9780439023481', 'publisher': 'Scholastic Press', 'genre': 'Distopia', 'page_count': 374, 'language': 'Inglês', 'summary': 'O primeiro livro da trilogia "Jogos Vorazes", que se passa em um futuro pós-apocalíptico onde adolescentes são selecionados para lutar até a morte em uma arena televisionada.', 'cover_image': 'link_to_cover_image_18.jpg', 'stock': 14, 'price': 8.50},
            {'title': 'Estilhaça-me', 'author': 'Tahereh Mafi', 'publication_date': '2011-11-15', 'isbn': '9780062085481', 'publisher': 'HarperCollins Publishers', 'genre': 'Ficção Adolescente', 'page_count': 338, 'language': 'Inglês', 'summary': 'O primeiro livro da série "Estilhaça-me", que segue a história de Juliette, uma garota com um toque fatal.', 'cover_image': 'link_to_cover_image_19.jpg', 'stock': 9, 'price': 11.25},
            {'title': 'O Nome do Vento', 'author': 'Patrick Rothfuss', 'publication_date': '2007-04-01', 'isbn': '9780575081406', 'publisher': 'DAW Books', 'genre': 'Fantasia', 'page_count': 662, 'language': 'Inglês', 'summary': 'O primeiro livro da série "A Crônica do Matador do Rei", uma narrativa sobre a vida de Kvothe, um músico e mago lendário.', 'cover_image': 'link_to_cover_image_20.jpg', 'stock': 13, 'price': 14.00}
        ]
    )

def downgrade():
    op.drop_table('books')