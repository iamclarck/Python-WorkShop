from requests_html import HTMLSession, HTML
import csv
import urllib.request
import requests
session = HTMLSession()


urls = ['https://bit.ly/2vqkYSu', 'https://bit.ly/3aqlYoH',
        'https://bit.ly/32DA0Ra']

for url in urls:
    response = requests.get(url, stream=True