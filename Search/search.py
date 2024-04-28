from sys import argv # Arguments
import typing # Dunno
from os import listdir # I'll need this

if len(argv) < 3: print("Usage: search (path\\to\\folder) (the rest is text. no double quotes!)") # If invalid number of arguments

directory = argv[1]

for file in listdir(directory): # Cycle over files in the directory
    with open(directory + "\\")