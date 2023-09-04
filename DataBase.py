from SqliteDB import SqliteDB
from FileIO import FileIO

class DataBase():
    def __init__(self):
        self.db = SqliteDB()
        self.db.connect("CIS41b")
        self.db.createTable()

    def build(self, website):
        df = FileIO.scrape_page(website)
        for index, row in df.iterrows():
            self.db.insert(tuple(row))

    def get_Co2_db(self):
        return self.db.readTable()

    def get_Co2_df(self):
        return self.db.readTableToDf()