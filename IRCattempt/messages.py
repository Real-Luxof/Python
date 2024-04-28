from time import sleep # Obvious.
from sys import argv # Obvious.
import requests # For getting messages.
import os # For clearing the screen.

serverIP = argv[1]

def cls(): # Clear the screen.
    os.system('cls' if os.name=='nt' else 'clear') 

while True:
    sleep(2)
    cls()
    messagelog = str.split(requests.get(serverIP).text, "\n")
    for message in messagelog: print(message)