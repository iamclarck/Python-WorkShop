import requests_html
from requests_html import HTMLSession,HTMLResponse,HTML

session = HTMLSession()

response = session.get('http://imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html

body = response.find('div.list.detail.sub-list')[0]

titles = body.find('.overview-top')

director = body.find('div.txt-block')[0]
print(director.text)

for a in titles:
    print('Title------>'+ a.find('h4')[0].text)
    genre = a.find('p.cert-runtime-genre span')
    for i in genre:
        print(i.text.split('|'))

    print(a.find('.outline')[0].text)
 
