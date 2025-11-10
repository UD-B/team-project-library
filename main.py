from classes.book import Book
from classes.library import Library
from classes.user import User


book1 = Book("potter", "j.k.rowling")
book2 = Book("chaim", "asher")

user1 = User("shay", 208795658,[])
user2 = User("yishay", 208795333,[])


library = Library()
library.add_book(book1)
library.add_user(user1)

print(library.borrow_book(208795658, book1.ISBN))
print(user1) 
# for book in user1.borrowed_books:
#     print(book)

