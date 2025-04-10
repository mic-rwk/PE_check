import sqlite3

class dbMenager:

    @classmethod
    def connect():
        return sqlite3.connect("zajecia.db")
    
    @classmethod
    def create_tables(connection):
        with connection:
            connection.execute(CREATE_BUILDING_TABLE)