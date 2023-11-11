# Loading

# Imports and Arguments
from sys import argv
import typing
if len(argv) == 1 or len(argv) > 2: print("Usage: flh (filename)")

# Variables
vars: dict = {}

# Functions
def isint(string: str) -> bool:
    """
    Determines if {string} is an integer.
    
    Example:
        if isint("1234"): print("Success!")
        else: print("Failure!")
    """
    try: int(string); return True
    except(ValueError): return False

def getsetvar(variable: str, value: typing.Any=None) -> typing.Any | bool:
    """
    If {value} is set to None, it will try to return the value of {variable}.
    If {variable} does not exist, it will return False.
    
    If {value} is set to anything other than None, it will set the value of {variable} to {value}.
    """
    if value == None:
        try: return vars[variable]
        except(KeyError): return False
    else: vars[variable] = value; return True

def console(line: str) -> None:
    """
    Performs console commands.
    console.out functions like print().
    console.in functions like input().
    
    Example (in FLHLang):
        console.out("Hello World!")
        console.in("Say Hi! > ")
    """
    # Initialize a few variables
    cline = line.split(".")
    inpar = []
    instr = []
    inparID = []
    instrID = []
    if cline[1].startswith("out("):
        for letter in cline.split("out(")[1]:
            if letter == "'" or letter == '"': instr.append(True), inparID.append()
    