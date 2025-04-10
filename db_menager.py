import sqlite3


CREATE_BUILDING_TABLE  = "CREATE TABLE IF NOT EXISTS Building (Building_ID TEXT PRIMARY KEY, " \
                                                                "Address TEXT NOT NULL)"

CREATE_CLASS_TABLE = "CREATE TABLE IF NOT EXISTS Class (Class_ID INTEGER PRIMARY KEY, " \
                    "Lecturer_ID INTEGER NOT NULL," \
                    "Start_Time TEXT NOT NULL, " \
                    "End_Time TEXT NOT NULL, " \
                    "Max_Capacity INTEGER NOT NULL DEFAULT 20, " \
                    "Enrolled_Count INTEGER NOT NULL," \
                    "Is_Cancelled INT, " \
                    "Subject_ID INTEGER NOT NULL," \
                    "Waiting_List_Count INT," \
                    "Room_ID INTEGER NOT NULL," \
                    "FOREIGN KEY(Subject_ID) REFERENCES Subject(Subject_ID)," \
                    "FOREIGN KEY(Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)," \
                    "FOREIGN KEY(Room_ID) REFERENCES Room(Room_ID) )"

CREATE_LECTURER_TABLE = "CREATE TABLE IF NOT EXISTS Lecturer (Lecturer_ID INTEGER PRIMARY KEY, " \
                                                            "First_Name TEXT NOT NULL," \
                                                            "Last_Name TEXT NOT NULL, " \
                                                            "Email TEXT NOT NULL)"

CREATE_ROOM_TABLE = "CREATE TABLE IF NOT EXISTS Room (Room_ID INTEGER PRIMARY KEY, " \
                                                    "Building_ID TEXT NOT NULL, " \
                                                    "FOREIGN KEY(Building_ID) REFERENCES Building(Building_ID))"

CREATE_STUDENT_TABLE = "CREATE TABLE IF NOT EXISTS Student (Index INTEGER PRIMARY KEY, " \
                                                            "First_Name TEXT NOT NULL, " \
                                                            "Last_Name TEXT NOT NULL, " \
                                                            "Major TEXT NOT NULL, " \
                                                            "Department TEXT NOT NULL," \
                                                            "Year_of_Study INTEGER NOT NULL)"

CREATE_SUBJECT_TABLE = "CREATE TABLE IF NOT EXISTS Subject (Subject_ID INTEGER PRIMARY KEY, " \
                                                            "Subject_Name TEXT NOT NULL)"

CREATE_RESERVATION_TABLE = "CREATE TABLE IF NOT EXISTS Reservation (Student_Index INTEGER, " \
                                                                    "Class_ID INTEGER,  " \
                                                                    "Reservation_Date TEXT NOT NULL, " \
                                                                    "Status TEXT NOT NULL, " \
                                                                    "Note TEXT NOT NULL," \
                                                                    "FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID)," \
                                                                    "FOREIGN KEY(Student_Index) REFERENCES Student(Index))"


class dbMenager:

    @classmethod
    def connect():
        return sqlite3.connect("zajecia.db")
    
    @classmethod
    def create_tables(connection):
        with connection:
            connection.execute(CREATE_BUILDING_TABLE)