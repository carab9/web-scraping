# web-scraping

This project is a web scraping and data visualization program. The goal of this project is to extract data of the top 10 countries’ emissions in 2017 and display them in a pie graph. The data is first scraped from a Wikipedia page called "List of countries by carbon dioxide emissions". The program parses and processes the data, stores it into the database, and then retrieves the data from the database and graphs it.

## Architecture

My code has an architecture with 3 layers: a UI layer that contains components required to enable user interaction with the application; a Business Layer that processes the input data; and a Data Layer that controls access logic components to access the data.

![image](https://github.com/carab9/web-scraping/blob/main/architecture.png?raw=true)

The UI layer consists of the UI and Graph classes. The Graph Class creates and displays  the pie graphs. The UI class creates the interface that the user interacts with: the main window.

The Business layer consists of the FileIO and Database classes. The FileIO class scrapes the necessary data from the webpage and processes it. The Database class creates a database and stores the data into the database. It also gets the data from the database for the UI layer to graph the data.

The Data layer consists of the SqliteDB class, which provides the SQL APIs to create, store and access the SQLite database 

## Requirements

Python
Python Libraries: pandas, sqlite3, matplotlib.figure, matplotlib.backends.backend_tkagg, tkinter, urllib.request, bs4
Run the program: python main.py

## Technical Skills

urllib and BeautifulSoup for web scraping, pandas dataframe for data processing, SQLite for database, matplotlib  Figure and FigureCanvasTkAgg for plotting graphs. Tkinter for GUIs.

## Results

This pie chart shows what percentage of the world total of CO2 emissions that the top 10 countries each emit.

![image](https://github.com/carab9/web-scraping/blob/main/web_scraping_pie_chart.png?raw=true)

