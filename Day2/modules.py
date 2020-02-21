from termcolor import colored
from random import choice,shuffle,randint
print(choice(['1','3','4']))
print(randint(1,100))
print(shuffle(['mango','apple','banana']))

text = colored("Hello world!",color="cyan",on_color="on_magenta",attrs=["blink"])
print(text)

# Pyfiglet
import pyfiglet
msg=input("what would you like to print: ")
color =input("what color: ")
valid_colors = ('red','green','blue','cyan','yellow','magenta','white')

if color not in valid_colors:
    color='magenta'
ascii_art = pyfiglet.figlet_format(msg)
color_ascii = colored(ascii_art,color=color)
print(color_ascii)

