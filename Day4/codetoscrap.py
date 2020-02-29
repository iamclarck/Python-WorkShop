import requests_html
from requests_html import HTMLSession,HTMLResponse,HTML
from bs4 import BeautifulSoup
urls = []
count = 1
quotes1 = []

for i in range(1,11):
    urls.append(f'http://quotes.toscrape.com/page/{i}')

for url in urls:

    session = HTMLSession()
    response = session.get(url).html
    source = response.html
    soup = BeautifulSoup(source,'lxml')

    # print(soup)
    # box = soup.find('')
    boxes = soup.find_all('div', class_='quote')
    # print(boxes)
    # print()
    for  box in boxes:
        quotes = box.find('span')
        quotes1.append(quotes.text)
        print(quotes1)
    print(count,end='')
    count = count + 1
    print()


# print(quotes)
# print(box)