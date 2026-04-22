# Task 1: Build a web scraper 

import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Top Headlines:\n")

titles = soup.find_all("span", class_="titleline")

for i, title in enumerate(titles[:10], start=1):
    print(f"{i}. {title.text}")