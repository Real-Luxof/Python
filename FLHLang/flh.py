"""The official Interpreter for FeelsLikeHellLang. The name is totally not a representation of what I feel when writing this code."""

# Imports and Arguments
from sys import argv
import typing
if len(argv) < 2 or len(argv) > 2: print("Usage: flh (filename)")

# Variables
vars: dict = {}
keywords: list = ["var", "out"]
operators: list = ["+", "-", "%", "/", "*", "^"]
varsetoperators: list = ["=", "+=", "-="]

# Functions
def throwerr(lineindex: int, wordindex: int, errmessage: str) -> None:
    """Throws an error to the user.

    Args:
        lineindex (int): What line number did the error happen at?
        wordindex (int): What word number did the error happen at?
        errmessage (str): The error message to throw.
    """
    print(f"ERR AT LINE {lineindex + 1}, WORD {wordindex + 1}: {errmessage}")
    quit()

def notoutofbounds(list: list, index: int) -> bool:
    """Checks if an index is out of bounds of a list.

    Args:
        list (list): The list to check.
        index (int): The index to check.

    Returns:
        bool: True if the index is not out of bounds, False otherwise.
    """
    try: list[index]; return True
    except(IndexError): return False

def isint(string: str) -> bool:
    """
    Determines if {string} is an integer.
    
    Example:
        if isint("1234"): print("Success!")
        else: print("Failure!")
    """
    try: int(string); return True
    except(ValueError): return False

def calculate(num1, op, num2):
    match op:
        case "+": return num1 + num2
        case "-": return num1 - num2
        case "%": return num1 % num2
        case "/": return num1 / num2
        case "*": return num1 * num2
        case "^": return pow(num1, num2)

def isvar(variable: str) -> bool:
    """Checks if a variable exists.

    Args:
        variable (str): The variable name.

    Returns:
        bool: True if the variable exists, false otherwise.
    """
    global vars
    try: vars[variable]; return True
    except(KeyError): return False

def getsetvar(variable: str, value: typing.Any=None) -> typing.Any | bool:
    """
    If {value} is set to None, it will try to return the value of {variable}.
    If {variable} does not exist, it will return False.
    
    If {value} is set to anything other than None, it will set the value of {variable} to {value}.
    """
    global vars
    if value == None:
        try: return vars[variable]
        except(KeyError): return False
    else: vars[variable] = value; return True

#def console(line: str) -> None:
#    """
#    Performs console commands.
#    console.out functions like print().
#    console.in functions like input().
#
#    Example (in FLHLang):
#        console.out("Hello World!")
#        console.in("Say Hi! > ")
#    """
#    # Initialize a few variables
#    cline = line.split(".")
#    inpar = []
#    instr = []
#    inparID = []
#    instrID = []
#    if cline[1].startswith("out("):
#        for letter in cline.split("out(")[1]:
#            if letter == "'" or letter == '"': instr.append(True), inparID.append()

def parsefile(pathtofile):

    f = open(pathtofile, "r")

    global vars
    global keywords
    global operators
    global varsetoperators
    file = f.readlines()
    parsedfile = []

    getvarflag = False
    calcflag = False

    for uncookedlineindex in range(len(file)):
        uncookedline = file[uncookedlineindex]
        # LET HIM COOK :fire:
        cookedline = uncookedline.split(" ")

        consoleflag = False
        parsedline = []

        for wordindex in range(len(cookedline)):
            word = cookedline[wordindex]
            if notoutofbounds(cookedline, wordindex + 1):
                nextword = cookedline[wordindex + 1]

            if word not in keywords and word not in vars and word not in operators and word not in varsetoperators and not getvarflag and not isint(word):
                throwerr(uncookedlineindex, wordindex, "UNDEFINED WORD")

            elif word in vars:
                if calcflag:
                    calcflag = False
                    continue
                if getvarflag:
                    continue

                getvarflag = True

                parsedline.append("getvar")
                parsedline.append(word)

            elif word in operators: pass

            match word:
                case "var":
                    getvarflag = True
                    parsedline.append("getvar")
                    parsedline.append(nextword)

                case "=":
                    if not getvarflag:
                        throwerr(uncookedlineindex, wordindex, "MISPLACED EQUAL SIGN")

                    getvarflag = False
                    getsetvar(parsedline[-1], nextword)

                case "+=":
                    if not getvarflag:
                        throwerr(uncookedlineindex, wordindex, "MISPLACED PLUS EQUAL SIGN")

                    if isvar(parsedline[-1]):
                        if not isint(getsetvar(parsedline[-1])):
                            throwerr(uncookedlineindex, wordindex + 1, "CANNOT ADD [STR] AND [INT]")

                        if not isvar(nextword):
                            if not isint(nextword):
                                throwerr(uncookedlineindex, wordindex + 1, "CANNOT ADD [INT] AND [STR]")
                        
                        elif not isint(getsetvar(nextword)):
                            throwerr(uncookedlineindex, wordindex + 1, "CANNOT ADD [INT] AND [STR]")

                        parsedline[-1] = int(getsetvar(parsedline[-1])) + int(nextword)
                        calcflag = True

                    elif isint(parsedline[-1]):
                        if not isint(nextword):
                            throwerr(uncookedlineindex, wordindex, "CANNOT ADD [INT] AND [STR]")
                        parsedline[-1] = int(parsedline[-1]) + int(nextword)

                    elif isint(nextword):
                        throwerr(uncookedlineindex, wordindex, "CANNOT ADD [STR] AND [INT]")
                    
                    parsedline[-1] = int(parsedline[-1]) + int(nextword)
                    calcflag = True

                case "-=":
                    if not getvarflag:
                        return f"ERR AT LINE {uncookedline + 1}, WORD {wordindex + 1}: MISPLACED MINUS EQUAL SIGN"
                    parsedline[-1] -= nextword
                    calcflag = True

                case "out":
                    consoleflag = True
                    parsedline.append(word)

        parsedfile.append(parsedline)
    
    return parsedfile

def interpret(parsedfile):
    global vars
    global keywords

    for lineindex in range(len(parsedfile)):
        for wordindex in range(lineindex):
            # Declare and get Variables
            pass

file = parsefile(argv[1])

with open("parsedresult", "w") as result:
    result.write(str(file))
