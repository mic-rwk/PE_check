import sqlite3

class dbMenager:

    @classmethod
    def connect():
        return sqlite3.connect("zajecia.db")