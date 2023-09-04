import requests
import shutil
import sys
import pandas as pd
from DataBase import DataBase
from UI import UI



def main():
    db = DataBase()
    db.build("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions")
    co2_db = db.get_Co2_db()
    co2_df = db.get_Co2_df()
    co2_df_sorted =  co2_df.sort_values('Co2', ascending=False)
    co2_df_top_10 = co2_df_sorted[1:11]

    others_percent = 100 - co2_df_top_10['Co2'].sum()
    print(others_percent)
    print(co2_df_top_10)

    co2_df_top_10.index = pd.RangeIndex(len(co2_df_top_10))
    print(co2_df_top_10)
    co2_df_top_10.loc[len(co2_df_top_10.index)] = ['Others', others_percent]
    print(co2_df_top_10)

    ui = UI()
    ui.run(co2_df_top_10)



if __name__ == '__main__':
    main()