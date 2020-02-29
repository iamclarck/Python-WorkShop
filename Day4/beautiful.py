import requests_html
from requests_html import HTMLSession,HTMLResponse,HTML
from bs4 import BeautifulSoup
import urllib
import csv
urls = []
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

csv_file = open('books.csv','w')
csv_writer = csv.writer(csv_file,lineterminator='\n')
csv_writer.writerow(['title','price','image_url'])
count = 1
for url in urls:
    session = HTMLSession()
    response = session.get(url).html
    source = response.html




soup = BeautifulSoup(source,'lxml')
# print(dir(soup))
box = soup.find('ol')
book = []
elements = box.find_all('li')
for element in elements:
    title = element.select('h3 a')[0]['title']
    price = element.find('p', class_='price_color')

    image = element.find('img')['src']
    image_url = 'http://books.toscrape.com/' + image
    book.append((title,price.text,image_url))
    csv_writer.writerow([title,price.text,image_url])
    

for i in book:
    print(i)
    print(count,end='')
    count = count + 1
    print()

csv_file.close()



# stock = element.find('p',class_='instock availability')
# print(stock.text)


# print(box)