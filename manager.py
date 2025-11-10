import json

class FileHandling:
    def __init__(self):
        pass
    def to_json(self, library):
        with open("books.json", "w") as file:
            file.write(self.library.list_of_books)

        with open("users.json", "w") as file:
            file.write(self.library.list_of_users)
        