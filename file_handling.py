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
    
    def serialize(self, libary: list[Library]):
        data = []
        for i in libary.list_of_users:
            dict_user = {"name" : i.name,
                         "id" : i.id,
                         "borrowed books" : i.borrowed_books
                         }
            data.append(dict_user)
        return data

    def json_book(self, library_atribute: list[object]):
        with open("json_book.json", "w") as f:
            json.dump(library_atribute, f, indent=4)


