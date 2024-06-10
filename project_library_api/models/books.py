from sqlalchemy import Column, Integer, String, Date, Text, DECIMAL
from project_library_api import db

class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="Identificador único para cada livro")
    title = Column(String(255), nullable=False, comment="O título do livro")
    author = Column(String(255), nullable=False, comment="O autor do livro")
    publication_date = Column(Date, comment="A data de publicação do livro")
    isbn = Column(String(13), unique=True, comment="Número padrão internacional do livro (ISBN)")
    publisher = Column(String(255), comment="A editora do livro")
    genre = Column(String(100), comment="O gênero ou categoria do livro (ex: Ficção, Não-Ficção)")
    page_count = Column(Integer, comment="O número total de páginas do livro")
    language = Column(String(50), comment="O idioma em que o livro está escrito")
    summary = Column(Text, comment="Um breve resumo ou descrição do conteúdo do livro")
    cover_image = Column(String(255), comment="Um link para a imagem da capa do livro")
    stock = Column(Integer, default=0, comment="O número de cópias disponíveis em estoque")
    price = Column(DECIMAL(10, 2), comment="O preço do livro")

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'publication_date': self.publication_date.strftime('%Y-%m-%d') if self.publication_date else None,
            'isbn': self.isbn,
            'publisher': self.publisher,
            'genre': self.genre,
            'page_count': self.page_count,
            'language': self.language,
            'summary': self.summary,
            'cover_image': self.cover_image,
            'stock': self.stock,
            'price': float(self.price) if self.price else None
        }