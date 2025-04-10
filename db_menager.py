import sqlite3


CREATE_BUILDING_TABLE  = "CREATE TABLE IF NOT EXISTS Building (Building_ID TEXT PRIMARY KEY, Adress TEXT NOT NULL)"

CREATE_CLASS_TABLE = "CREATE TABLE IF NOT EXISTS Class (Class_ID INTEGER PRIMARY KEY, Lecturer_ID INTEGER NOT NULL" \
"Start_Time TEXT NOT NULL, End_Time TEXT NOT NULL, Max_Capacity INTEGER NOT NULL, Enrolled_Count INTEGER NOT NULL" \
"Is_Cancelled TEXT NOT NULL, Subject_ID INTEGER NOT NULL)"

CREATE_LECTURER_TABLE = "CREATE TABLE IF NOT EXISTS Lecturer (Lecturer_ID INTEGER PRIMARY KEY, First_Name TEXT NOT NULL," \
"Last_Name TEXT NOT NULL, Email TEXT NOT NULL)"
CREATE_ROOM_TABLE = ""
CREATE_STUDENT_TABLE = ""
CREATE_SUBJECT_TABLE = ""
CREATE_RESERVATION_TABLE = ""


class dbMenager:

    @classmethod
    def connect():
        return sqlite3.connect("zajecia.db")
    
    @classmethod
    def create_tables(connection):
        with connection:
            connection.execute(CREATE_BUILDING_TABLE)