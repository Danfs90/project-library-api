class Book:
    def __init__(self, title, author, isbn, publication, db = None):
        self.db = db
        self.title = title
        self.author = author
        self.isbn = isbn        # codigo de barras do livro
        self.publication = publication       # ano de publicação
