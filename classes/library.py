


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
                        print(f'the book: {j.title} is borrowed')
                        return
                    else:
                        print("the book doesn't exist! ")
                        return
            print("user doesn't exist!")
            return

    def return_book(self, user_id, book_isbn):
        for i in self.list_of_users:
            if i.id == user_id:
                for j in self.list_of_books:
                    if j.ISBN == book_isbn and not j.is_availabale:
                        i.borrowed_books.reamove(j)
                        print(f'the book: {j.title} is return')
                        return
                    else:
                        print("the book doesn't exist! ")
                        return    
            print("user doesn't exist!")
            return
        
    def list_available_books(self):
        return [str(i) for i in self.list_of_books if i.is_availabale]

    def search_book(self, title):
        for i in self.list_of_books:
            if i.title == title:
                return i.title
        return "not found!"
