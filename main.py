from classes.book import Book
from classes.library import Library
from classes.user import User
import manager

book1 = Book("potter", "j.k.rowling")
book2 = Book("chaim", "asher")

user1 = User("shay", 208795658,[])
user2 = User("yishay", 208795333,[])


library1 = Library()
library1.add_book(book1)
library1.add_user(user1)

print(library1.borrow_book(208795658, book1.ISBN))
print(user1)
handle = manager.FileHandling()
handle.book_to_json(library1)