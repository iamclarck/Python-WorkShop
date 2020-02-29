import requests_html
from requests_html import HTMLSession, HTMLResponse, HTML
from bs4 import BeautifulSoup
import urllib
import csv

# titles = []
# grosses = []
# weekends = []
# weeks = []
session = HTMLSession()


urls = ['https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth', 'https://www.imdb.com/movies-coming-soon/?ref_=inth_cs',
        'https://www.imdb.com/chart/top/?ref_=nv_mv_250', 'https://www.imdb.com/search/title/?genres=horror&start=1&explore=title_type.genres&ref_=adv_nxt']


for i in urls:
    response = session.get(i)
    source = response.html
    soup = BeautifulSoup(source, 'lxml')





    csv_file = open('imdbScraped1.csv', 'w')
    csv_writer = csv.writer(csv_file, lineterminator='\n')
    
    csv_writer.writerow(['TITLE', 'RATING', 'RUNTIME', 'GENRE',
                        'SUMMARY', 'DIRECTOR', 'ACTORS'])

    names = html.find('.nm-title-overview-widget-layout')
    for name in names:
        title = name.find('h4 a', first=True).text

        runTime = name.find('.cert-runtime-genre time', first=True).text
        genre = name.find('.cert-runtime-genre span', first=True).text

        try:
            rating = name.find('.rating_tx', first=True).text
        except Exception as identifier:
            rating = 'None'

        outline = name.find('.outline', first=True).text

        director = name.find('.txt-block span a', first=True).text

        stars = name.find('.txt-block a')

        # print("ACTORS")
        iter_stars = iter(stars)
        next(iter_stars)

        for star_name in iter_stars:
            print(star_name.text)
        print(type(iter_stars))

        csv_writer.writerow([title, rating, runTime, genre,
                            outline, director, star_name.text])
csv_file.close()














csv_file = open('imdb.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['titles', 'grosses', 'weekends', 'weeks'])


body = soup.find('tbody')
rows = body.find_all('tr')
for row in rows:

    element = row.find('td', class_='titleColumn').a.text
    titles.append(element)

    gross = row.find('td', class_='ratingColumn').text.strip()
    grosses.append(gross)

    weekend = row.find('span', class_='secondaryInfo').text.strip()
    weekends.append(weekend)

    week = row.find('td', class_='weeksColumn').text.strip()
    weeks.append(week)

    csv_writer.writerow([element, gross, weekend, week])
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
