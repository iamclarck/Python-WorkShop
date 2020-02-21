
# final = {num:num*num for num in [1,2,3,4]}

# print(final)
import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000!")
header = colored(header,color="magenta")
print(header)
user_input = input("what would you like to search for? ")
url="http://icanhazdadjoke.com/search"
response = requests.get(url,
headers={ "Accept":"application/json"},
  params = { "term":user_input} ).json()

# print(f'your request to {url} come back with code {response}')
num_jokes =response["total_jokes"]
results = response["results"]
if num_jokes>1:
    print(f"I found {num_jokes} jokes about {user_input}. Here is one..")
    print(choice(results)["joke"])

elif num_jokes==1:
    print(f"I found one joke about{user_input}")
    print(results["joke"])

else:
    print(f"sorry we could not find a joke with your term:{user_input}")
    