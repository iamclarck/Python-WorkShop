import requests
s = requests.session()

urls = ['https://bit.ly/2vqkYSu', 'https://bit.ly/3aqlYoH',
        'https://bit.ly/32DA0Ra']

names = ['first','second','third']
for url in range(len(urls)):      
    response = s.get(urls[url])
    fp = open(names[url] +'.pdf','wb')
    fp.write(response.content)
    fp.close()

        

# epochtime - seconds from 1st jan 1997