import sqlite3
import os
import pandas as pd

class SqliteDB:
    # Constructor
    def __init__(self):
        self.sqliteConnection = None
        self.dbname = ""

    # Destructor
    def __del__(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
            os.remove(self.dbname)

    # Create a SQLite database
    def connect(self, dbname):
        try:
            self.dbname = dbname
            self.sqliteConnection = sqlite3.connect(dbname)
            cur = self.sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            query = "SELECT sqlite_version();"
            cur.execute(query)
            rec = cur.fetchall()
            print("SQLite Database Version is: ", rec)
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    # Create a table for the database
    def createTable(self):
        try:
            cur = self.sqliteConnection.cursor()
            query = """CREATE TABLE Database (
                                       Country TEXT PRIMARY KEY,
                                       Co2 REAL NOT NULL)"""
            cur.execute(query)
            self.sqliteConnection.commit()
            print("SQLite table created")
        except sqlite3.Error as error:
            print("Table exists: ", error)

    # Get all the records of a table
    def readTable(self):
        rec = None
        try:
            cur = self.sqliteConnection.cursor()
            query = """SELECT * from Database"""
            cur.execute(query)
            rec = cur.fetchall()
            print("Total rows are:  ", len(rec))
        except sqlite3.Error as error:
            print("Failed to read data from table", error)
        finally:
            return rec

    def readTableToDf(self):
        df = None
        try:
            query = """SELECT * from Database"""
            df = pd.read_sql_query(query, self.sqliteConnection)
            print("Total rows are:  ", len(df.index))
        except sqlite3.Error as error:
            print("Failed to read data from table", error)
        finally:
            return df

    # Build a query for inserting a record
    def _build_insert_query(self):
        # Get all column names from the table
        cur = self.sqliteConnection.cursor()
        query = """SELECT name from PRAGMA_TABLE_INFO('Database')"""
        cur.execute(query)
        rec = cur.fetchall()
        cols = ', '.join([r[0] for r in rec])
        vals = ", ".join("?" * len(rec))
        query = 'INSERT into Database ({}) VALUES ({})'.format(cols, vals)
        return query

    def insert(self, tup):
        try:
            query = self._build_insert_query()
            cur = self.sqliteConnection.cursor()
            cur.execute(query, tup)
            self.sqliteConnection.commit()
            print("Inserted successfully into table")
        except sqlite3.Error as error:
            print("Failed to insert: ", error)

        # Search records by the name and return a list of tuples (id, name, html)

    def search(self, name):
        rec = None
        try:
            cursor = self.sqliteConnection.cursor()
            sel = 'SELECT * FROM Database WHERE name == "{0}"'.format(name)
            cursor.execute(sel)
            rec = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to search:", error)
        finally:
            return rec