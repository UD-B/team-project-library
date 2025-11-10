import json
import classes.library

class FileHandling:
    def __init__(self):
        pass

    def serialize(self, object_list: list[object]):
        serialized = (obj.__dict__ for obj in object_list)

    def json_book(self, library_atribute: list[object]):
        with open("books.json", "")







    # def book_to_json(self, library):
    #     with open("books.json", "w") as file:
    #       json.dump(library.list_of_books, file)
    # def user_to_json(self, library):
    #     with open("users.json", "w") as file:
    #         file.write(library.list_of_users)
        