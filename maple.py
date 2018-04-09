import requests
from bs4 import BeautifulSoup

url = "http://maplestory.nexon.co.jp/"
response = requests.get(url)
print(response.text)
soup = BeautifulSoup(response.text, "lxml")

title = soup.title.string
print(title)