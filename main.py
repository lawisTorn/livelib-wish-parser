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
        name_books = soup.find_all('a', class_='brow-book-name with-cycle')
        
        for book in name_books:
            print(book.get('href'), book.text)
    else:
        print(f"Failed to retrieve page {x}")