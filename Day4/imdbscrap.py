import requests_html
from requests_html import HTMLSession,HTMLResponse,HTML
from bs4 import BeautifulSoup
import urllib
import csv

titles = []
grosses = []
weekends = []
weeks = []
session = HTMLSession()
response = session.get('https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht').html
source = response.html
soup = BeautifulSoup(source,'lxml')

csv_file = open('imdb.csv','w')
csv_writer = csv.writer(csv_file,lineterminator='\n')
csv_writer.writerow(['titles','grosses','weekends','weeks'])


body = soup.find('tbody')
rows =  body.find_all('tr')
for row in rows:
        
    element = row.find('td',class_='titleColumn').a.text
    titles.append(element)

    gross = row.find('td', class_='ratingColumn').text.strip()
    grosses.append(gross)

    weekend = row.find('span', class_='secondaryInfo').text.strip()
    weekends.append(weekend)

    week = row.find('td', class_='weeksColumn').text.strip()
    weeks.append(week)


    csv_writer.writerow([element,gross,weekend,week])
csv_file.close()




# for i in week:
#     weeks.append(i.text.strip())
# print('-------------------Weeks-----------------')
# print(weeks)

# for i in weekend:
#     weekends.append(i.text.strip())
# print('-------------------Weekends-----------------')
# print(weekends)


# for i in gross:
#     grosses.append(i.text.strip())
# print('-------------------Grosses-----------------')
# print(grosses)

# for elements in element:
#     titles.append(elements.a.text)
# print('-------------------Titles-----------------')
# print(titles)
