import requests
from bs4 import BeautifulSoup

URL = "https://ftmscan.com/tx/0x1216efaf1cafb71ecd0d7d828ff760d90e9315b33f30b038af200c1af07a6ed6"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="wrapperContent")

print(results.prettify())