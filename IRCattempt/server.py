import os # Used for clearing the screen and to download some modules.
from time import sleep # Obvious.
from sys import stdout # for stdout.flush()
try: from flask import Flask, request # Used for setting up the server.
except(ImportError): os.system("python -m pip install flask"); from flask import Flask, request

server = Flask('')

@server.route("/")
def home():
    with open("serverdata", "r") as serverdata: return serverdata.read()

@server.route("/send", methods=['POST'])
def send():
    message = request.form['message']
    with open("serverdata", "r+") as serverdata:
        messagelog = serverdata.read()
        serverdata.write(f"{message}\n")
    return 'Done.'

port = int(input("Port > "))

server.run(host="0.0.0.0", port=port)
