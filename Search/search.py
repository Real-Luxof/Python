from sys import argv # Arguments
import typing # Dunno
from os import listdir # I'll need this

if len(argv) < 2:
    print("Usage: search (path\\to\\folder) (the rest is text. no double quotes!)")
# If invalid number of arguments, tell them how to use it.
del argv[0]
directory = " ".join(argv)

for file in listdir(directory): # Cycle over files in the directory
    with open(f"{directory}\\{file}"):
        