class Book:
    def __init__(self, input_title, input_genre, input_author, id = None):
        self.title = input_title
        self.genre = input_genre
        self.author = input_author
        self.id = id