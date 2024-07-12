from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_page_data(name, page):
    url = f'https://www.livelib.ru/reader/{name}/wish/~{page}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Ошибка загрузки страницы {page}")
        return []
    
    soup = BeautifulSoup(response.text, 'lxml')
    name_books = soup.find_all('a', class_='brow-book-name with-cycle')
    page_data = []

    for book in name_books:
        book_title = book.text.strip()
        book_authors = []
        parent_element = book.find_parent('div', class_='brow-data')
        if parent_element:
            authors = parent_element.find_all('a', class_='brow-book-author')
            for author in authors:
                book_authors.append(author.text.strip())
        
        page_data.append({
            'Book': book_title,
            'Authors': ', '.join(book_authors)
        })
    
    return page_data

def main():
    pages = int(input("Кол-во страниц: "))
    name = input("Имя на LiveLib: ")
    book_data = []

    for x in range(1, pages + 1):
        print(f"Загружается страница {x}...")
        page_data = get_page_data(name, x)
        book_data.extend(page_data)
    
    df = pd.DataFrame(book_data)
    df.to_excel('book_data.xlsx', index=False)
    
    print("Данные сохранены в book_data.xlsx")

if __name__ == "__main__":
    main()