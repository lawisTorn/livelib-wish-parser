from bs4 import BeautifulSoup
import requests

pages = int(input("All pages: "))
name = input("Name on LiveLib: ")

for x in range(1, pages + 1):
    url = f'https://www.livelib.ru/reader/{name}/wish/~{x}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        print(soup.prettify())
    else:
        print(f"Failed to retrieve page {x}")
