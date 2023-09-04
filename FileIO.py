from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class FileIO:
    def __init__(self):
        pass

    @staticmethod
    def _open_html_site(html_site):
        html = urlopen(html_site)
        return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def scrape_page(website):
        soup = FileIO._open_html_site(website)
        table = soup.find('table', class_=['wikitable', 'sortable'])

        df = pd.DataFrame(columns=['Country', 'Co2'])

        try:
            table_body = table.find('tbody')
            if table_body:
                rows = table_body.find_all('tr')
                for row in rows:
                    # Get headers
                    cols = row.find_all('th')
                    cols = [x.text.strip() for x in cols]
                    if cols:
                        if '2017(% of world)' in cols:
                            index = cols.index('2017(% of world)')
                            index += 1

                    cols = row.find_all('td')
                    cols = [x.text.strip() for x in cols]
                    if cols:
                        country = cols[0]

                        co2 = float(cols[index][:-1])
                        df.loc[len(df.index)] = [country, co2]
        except ValueError as exc:
            print("Error:", str(exc))
            raise RuntimeError from exc
        finally:
            return df