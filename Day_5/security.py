from datetime import datetime as dt
import time

# today8am = today.replace(hour=8, minute=0, second=0, microsecond=0)

# if(today > today8am):
#     print("Hello")
host_path = r'C:\Windows\System32\drivers\etc\hosts'
hosts = r'hosts'
redirect = '127.0.0.1'
weblist = ['www.facebook.com','facebook.com','youtube.com','www.youtube.com','twitter.com']
date1 = dt(dt.now().year, dt.now().month, dt.now().day, 15)
date2 = dt(dt.now().year, dt.now().month, dt.now().day, 16,47)


while True:
    today = dt.now()  # today object is created

    if( date1 < today < date2 ):
        print('Working hours!',dt.now())
        with open(host_path,'r+') as file:
            content = file.read()
            for website in weblist:
                if(website in content):
                    pass
                else:
                    file.write(redirect+ ' ' +website+ "\n")

    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0) # start line from 0 index
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)
            file.truncate()  # it will keep latest content of file and delete privious content
        print("Fun Time", dt.now())

    time.sleep(1)
