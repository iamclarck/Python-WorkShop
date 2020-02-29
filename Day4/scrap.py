import requests_html
from requests_html import HTMLSession,HTMLResponse

session = HTMLSession()

response = session.get('http://172.16.104.50/').html
# print(response)

response.render() # to scrap javascript code

# block = response.find('.article,#test')
# print('------------------Headings---------------')
# for a in block:
#     headline = a.find('h2')
#     for headlines in headline:
#          print(headlines.text)

# print('------------------Summaries---------------')

# sum = []
# for b in block:
#     summary = b.find('p')[0]
#     sum.append(summary.text)
# for summaries in sum:
#     print(summaries)


footer = response.find('#footer')[0]
para = footer.find('p')
for i in para:
    print(i.text)


    