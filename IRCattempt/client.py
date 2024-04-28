import os # Used for clearing the screen, to download some modules, and to show messages.
from time import sleep # Obvious.
from sys import stdout # for stdout.flush()
try: import requests
except(ImportError): os.system("python -m pip install requests"); import requests # Used to connect to a server.
from threading import Thread # For updating messagelog.

validselected = False
serverIP = ""
message = ""
content = {}

def typewrite(message, delay): # Typewriter effect.
    for word in message:
        for char in word:
            print(char, end="")
            stdout.flush()
            sleep(delay)
    print()
def cls(): # Clear the screen.
    os.system('cls' if os.name=='nt' else 'clear') 

typewrite("IRC Attempt", 0.2)
typewrite("Bro tip: just type 'quit()' instead of a message to quit.", 0.0125)

serverIP = input("\nServer IP Address (with port) > ")
username = input("Username > ")
serverIP = f"http://{serverIP}"

os.system(f"start python messages.py {serverIP}")
while True:
    cls()
    message = input("> ")
    if message == "quit()": break
    else:
        content = {"message": f"<{username}> {message}"}
        requests.post(serverIP + "/send", data=content)
