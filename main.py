from classes.book import Book
from classes.library import Library
from classes.user import User
# from manager import FileHandling

book1 = Book("potter", "j.k.rowling")
book2 = Book("chaim", "asher")

user1 = User("shay", 208795658,[])
user2 = User("yishay", 208795333,[])


library = Library()
library.add_book(book1)
library.add_user(user1)

# file1 = FileHandling()
# file1.json_book(library.list_of_books)

print(library.list_of_books[0].author)
# print(a)