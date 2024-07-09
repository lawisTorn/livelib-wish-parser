from bs4 import BeautifulSoup
import requests

pages = int(input("all pages: "))
name = input("name on livelib: ")

for x in range(1,pages):
    data = requests.get('https://www.livelib.ru/reader/{name}/wish/~{x}')

