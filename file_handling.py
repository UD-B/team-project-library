from datetime import date
import json
from os import name
from turtle import done
from classes.book import Book
from classes.library import Library
from classes.user import User

class FileHandling:
    def __init__(self):
        pass

    def serialize(self, libary: list[Library]):
        data = []
        for i in libary.list_of_books:
            dict_book = {"title" : i.title,
                         "author" : i.author,
                         "ISBN" : i.ISBN,
                         "is_availabale" : i.is_availabale
                         }
            data.append(dict_book)
        return data

    def json_book(self, library_atribute: list[object]):
        with open("json_book.json", "w") as f:
            json.dump(self.serialize(library_atribute), f, indent=4)







