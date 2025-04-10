import sqlite3


CREATE_BUILDING_TABLE  = "CREATE TABLE Building (Building_ID TEXT PRIMARY KEY, Adress TEXT NOT NULL)"

class dbMenager:

    @classmethod
    def connect():
        return sqlite3.connect("zajecia.db")
    
    @classmethod
    def create_tables(connection):
        with connection:
            connection.execute(CREATE_BUILDING_TABLE)