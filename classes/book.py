import uuid

class Book:
    def __init__(self, title, author, is_availabale =True):
        self.title = title
        self.author = author
        self.ISBN = 12345
        self.is_availabale = is_availabale
        
    def __str__(self):
        return f'title: {self.title}, author: {self.author}, ISBN: {self.ISBN}, is_availabale: {self.is_availabale}'
    
