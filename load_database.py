import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Charlotte", "Bronte")
author_repository.save(author1)

book1 = Book("Jane Eyre", "Fiction", author1)
book_repository.save(book1)