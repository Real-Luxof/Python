print("Send a key to any window passively so you can leave your computer and do some other stuff.\nIt's like an autoclicker for keyboards.")
key = input("key > ")
delay = float(input("delay between each key press > "))
times = int(input("how many times? 0 or below defaults to infinite > "))

from time import sleep
try: import keyboard
except(ModuleNotFoundError): from os import system; system("pip install keyboard"); import keyboard

print("You have 5 seconds to go that window you wanted to automatically press a key in.")
sleep(5)
print("Time's up!")

if times <= 0:
    while True:
        keyboard.send(key)
        sleep(delay)
else:
    for i in range(times):
        keyboard.send(key)
        sleep(delay)

print("Success!")