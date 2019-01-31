from project import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    author = db.Column(db.String(24))


    def __init__(self, title, genre, author):
        self.title = title
        self.genre = genre
        self.author = author


    def __repr__(self):
        return f'{self.title} by {self.author} is a {self.genre} book. Book ID: {self.id}'
