# from .book import Book
# from .user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book):
        self.list_of_books.append(book)

    def add_user(self, user):
        self.list_of_users.append(user)

    def borrow_book(self, user_id, book_isbn):
        for i in self.list_of_users:
            if i.id == user_id:
                for j in self.list_of_books:
                    if j.ISBN == book_isbn and j.is_availabale:
                        j.is_availabale = False
                        i.borrowed_books.append(j)
                        return f'the book: {j.title} is borrowed  '
                    else:
                        return "the book doesn't exist! "
            return "user doesn't exist!"

    def return_book(self, user_id, book_isbn):
        for i in self.list_of_users:
            if i.id == user_id:
                for j in self.list_of_books:
                    if j.ISBN == book_isbn and j.is_availabale == False:
                        i.borrowed_books.reamove(j)
                        return f'the book: {j.title} is return'
                    else:
                        return "the book doesn't exist! "    
            return "user doesn't exist!"
        
    def list_available_books(self):
        pass

    def search_book(self, title):
        pass
