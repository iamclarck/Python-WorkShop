from requests_html import HTMLSession, HTML
import csv
import urllib.request
import requests
session = HTMLSession()

pdfs = ['1','2','3']
urls = ['https://bit.ly/2vqkYSu', 'https://bit.ly/3aqlYoH',
        'https://bit.ly/32DA0Ra']

for url in urls:
    response = requests.get(url, stream = True) 
    for a in pdfs:

        with open(f"{a}.pdf","wb") as pdf: 
            for chunk in response.iter_content(chunk_size=1024):
    
            # writing one chunk at a time to pdf file 
                if chunk: 
                    pdf.write(chunk) 
