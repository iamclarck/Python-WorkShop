import requests_html
from requests_html import HTMLSession,HTMLResponse,HTML

session = HTMLSession()

# response = session.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').html
response = session.get('http://imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html

body = response.find('tbody')[0]

# row = body.find('tr')
# for i in row:
#     title = i.find(' .titleColumn a')[0]
#     rating = i.find(' .imdbRating')[0]
#     print('Title--->' + title.text)
#     print('Rating----> '+ rating.text)
#     print()


rows = body.find('h4')
for i in rows:
    title = i.find('title')[0]
    print(title)

