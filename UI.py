from Graph import Graph
from tkinter import *

class UI:
    blackboard = None

    def __init__(self):
        self.window = Tk()
        self.window.title("Web Scraping")
        self.window.geometry("950x600")

    def run(self, df):
        g = Graph(df)
        g.display_pie_chart(self.window)
        self.window.mainloop()