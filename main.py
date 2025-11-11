from classes.book import Book
from classes.library import Library
from classes.user import User
import file_handling



arr_books = [Book("potter", "j.k.rowling"), Book("chaim", "asher"), Book("ring", "guy guy")]
arr_users = [User("shay", 208795658,[]), User("yishay", 208795333,[]), User("zeava", 2087953,[])]


library1 = Library()

for book in arr_books:
    library1.add_book(book)

for user in arr_users:
    library1.add_user(user)

print(library1.borrow_book(208795658, 587658767))
# print([str(i) for i in arr_books]) 

print(library1.list_available_books())

search_book = library1.search_book("potter")
print(search_book)

manager1 = file_handling.FileHandling()
manager1.json_book(library1) 
choice = input("")
if choice == "4":
    book_name = input("whats the name of the book you want to return: ")
if book_name in library1.list_