import threading
import requests
import time
urls = ['https://bit.ly/2vqkYSu', 'https://bit.ly/3aqlYoH',
        'https://bit.ly/32DA0Ra']

def download_save(url):
    response = requests.get(url)
    print(response.status_code)
    # f = open(f'{url}.pdf','wb')
    # f.write(response.content)
    # f.close()


t1 = time.time()
threads = []
for url in urls:
    th = threading.Thread(target=download_save,args=[url])
    th.start()
    threads.append(th)

for thread in threads:
    thread.join()
    # download_save(url)

t2 = time.time()

print(t2-t1)