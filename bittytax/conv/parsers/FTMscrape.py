import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36')}

def get_data(url):
    response = requests.get(url)
    return response

df = pd.read_excel(r"C:\Users\jonat\OneDrive\Crypto\Crypto Transactions\Transaction History\Defi\FTM\Transactions.xlsx")

df['URL'] = "https://ftmscan.com/tx/"+df['Txhash']

df['result'] = ""

for i in range(0,504):
    page = get_data(df.loc[i]['URL'])
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        results = soup.find(id="wrapperContent").get_text().split("For ")
        result = results[len(results)-1]
        df.at[i,'result'] = result
    except:
        continue



df.to_excel(r"C:\Users\jonat\OneDrive\Crypto\Crypto Transactions\Transaction History\Defi\FTM\Transactions_Scraped.xlsx")


# print(result)

# URL = "https://ftmscan.com/tx/0x1216efaf1cafb71ecd0d7d828ff760d90e9315b33f30b038af200c1af07a6ed6"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# ]results = soup.find(id="wrapperContent").get_text().split("For ")
# result = results[len(results)-1

# print(result)