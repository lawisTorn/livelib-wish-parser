from bs4 import BeautifulSoup
import requests
import pandas as pd

pages = int(input("Кол-во страниц: "))
name = input("Имя на LiveLib: ")

book_data = []

for x in range(1, pages + 1):
    url = f'https://www.livelib.ru/reader/{name}/wish/~{x}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        name_books = soup.find_all('a', class_='brow-book-name with-cycle')
        
        for book in name_books:
            book_title = book.text.strip()
            book_authors = []
            parent_element = book.find_parent('div', class_='brow-data')  
            if parent_element:
                authors = parent_element.find_all('a', class_='brow-book-author')
                for author in authors:
                    book_authors.append(author.text.strip())
            
            book_data.append({
                'Book': book_title,
                'Authors': ', '.join(book_authors)
            })
    else:
        print(f"Ошибка загрузки страницы {x}")

df = pd.DataFrame(book_data)

df.to_excel('book_data.xlsx', index=False)

print("сохраненно в папке со скриптом book_data.xlsx")