from re import search
from classes.book import Book
from classes.library import Library
from classes.user import User
import manager

arr_books = [Book("potter", "j.k.rowling"), Book("chaim", "asher"), Book("ring", "guy guy")]
arr_users = [User("shay", 208795658,[]), User("yishay", 208795333,[]), User("zeava", 2087953,[])]


<<<<<<< HEAD
library1 = Library()
library1.add_book(book1)
library1.add_user(user1)

print(library1.borrow_book(208795658, book1.ISBN))
print(user1)
handle = manager.FileHandling()
handle.book_to_json(library1)
=======
library = Library()

for book in arr_books:
    library.add_book(book)

for user in arr_users:
    library.add_user(user)

print(library.borrow_book(208795658, 587658767))
# print([str(i) for i in arr_books]) 

print(library.list_available_books())

search_book = library.search_book("potter")
print(search_book)
>>>>>>> c70a31610beb3234671c851d29abfb17982ebe6f
