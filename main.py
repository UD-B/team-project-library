from random import choice
from classes.book import Book
from classes.library import Library
from classes.user import User
import file_handling



library1 = Library()

choice = None
while choice != "7":
    print("1. Add Book\n2. Add User\n3. Borrow Book\n7. Save & Exit: ")
    choice = input("enter your choice: ")
    
    if choice  == "1":
        user_book_title = input("enter your title of book: ")
        user_book_author = input("enter your title of book: ")
        book1 = Book(user_book_title, user_book_author)
        library1.add_book(book1)
        print(f"the book {user_book_title}, {user_book_author} added")
        
    elif choice == "2":
        user_name = input("enter a username: ")
        user_id = input("enter a user ID: ")
        user1 = User(user_name, user_id)
        library1.add_user(user1)
        print(f"the user {user_name}, {user_id} added")
        
    elif choice == "3":
        user_id = input("enter a user ID: ")
        book_isbn = input("enter a book isbn: ")
        library1.borrow_book(user_id, book_isbn)
    
    elif choice == "4":
        user_ID = input("enter a user ID to return: ")
        book_isbn = input("enter a book isbn to return: ")
        library1.return_book(user_ID, book_isbn)
    
    elif choice == "5":
        print(library1.list_available_books())
        
    elif choice == "6":
        user_search = input("enter a title of book to search: ")
        print(library1.search_book(user_search))    
        
    elif choice == "7":
        break
    else:
        print("Invalid choice, try again.")

manager1 = file_handling.FileHandling()
serialize_list_books = manager1.serialize(library1)
manager1.json_book(serialize_list_books) 

