"""The official Interpreter for FeelsLikeHellLang. The name is totally not a representation of what I feel when writing this code."""
import math
# Imports and Arguments
from sys import argv
import typing
from ast import literal_eval
if len(argv) < 2 or len(argv) > 2: print("Usage: flh (filename)")

# Variables
vars: dict = {}
vars_list: list = [] # Used for the parser to figure shit out.
keywords: list = ["var", "out"]
operators: list = ["+", "-", "%", "/", "*", "^"]
varsetoperators: list = ["=", "+=", "-="]

# Functions
def throwerr(error_info: tuple[int, int], errmessage: str) -> None:
    """Throws an error to the user.

    Args:
        error_info (tuple): Info about the error. First element is the line index, second is the word index.
        errmessage (str): The error message to throw.
    """
    line_index = error_info[0]
    word_index = error_info[1]
    print(f"ERR AT LINE {line_index + 1}, WORD {word_index + 1}: {errmessage}")
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
    Determines if string is an integer.
    
    Example:
        if isint("1234"): print("Success!")
        else: print("Failure!")
    """
    try: int(string); return True
    except(ValueError): return False

def calculate(num1: int, op: str, num2: int):
    """Literally the name."""
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

def givetype(variable: str) -> typing.Any:
    """Checks if a string is actually a string representation of another type.

    Args:
        variable (str): The string to be checked.

    Returns: variable, but without the string representation.
    """
    if isint(variable): return int(variable)
    else:
        try:
            return literal_eval(variable)
        except(SyntaxError):
            return variable
        except(ValueError):
            return variable

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
    else: vars[variable] = givetype(value); return True

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

# The parser-lexer-compiler whatever thing
def parsefile(pathtofile):

    f = open(pathtofile, "r")

    global vars_list
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
            error_info = (uncookedlineindex, wordindex)
            error_info_nextword = (uncookedlineindex, wordindex + 1)
            word_is_defined = False

            if notoutofbounds(cookedline, wordindex + 1): nextword = cookedline[wordindex + 1]

            if getvarflag: word_is_defined = True

            if word in vars_list:
                if calcflag:
                    calcflag = False
                    word_is_defined = True
                    continue
                elif getvarflag:
                    word_is_defined = True
                    continue

                getvarflag = True
                word_is_defined = True

                parsedline.append("getvar")
                parsedline.append(word)

            elif word in operators: word_is_defined = True

            match word:
                case "var":
                    getvarflag = True
                    word_is_defined = True

                    parsedline.append("getvar")
                    vars_List.append(nextword)
                    parsedline.append(nextword)

                case "=":
                    if not getvarflag:
                        throwerr(error_info, "MISPLACED EQUAL SIGN")

                    getvarflag = False
                    word_is_defined = True

                    parsedline.append(nextword)
                    getsetvar(parsedline[-1], nextword)

                case "+=":
                    if not getvarflag:
                        throwerr(error_info, "MISPLACED PLUS EQUAL SIGN")

                    if getvarflag:
                        if isvar(nextword):
                            try:
                                getsetvar(parsedline[-1]) + getsetvar(nextword)
                            except(TypeError):
                                throwerr(error_info, "CANNOT ADD DUE TO TYPE DIFFERENCE")
                        else:
                            try:
                                getsetvar(parsedline[-1]) + givetype(nextword)
                            except(TypeError):
                                throwerr(error_info, "CANNOT ADD DUE TO TYPE DIFFERENCE")

                    elif isvar(nextword):
                        try:
                            givetype(parsedline[-1]) + getsetvar(nextword)
                        except(TypeError):
                            throwerr(error_info, "CANNOT ADD DUE TO TYPE DIFFERENCE")

                    else:
                        try:
                            givetype(parsedline[-1]) + givetype(nextword)
                        except(TypeError):
                            throwerr(error_info, "CANNOT ADD DUE TO TYPE DIFFERENCE")

                    calcflag = True
                    word_is_defined = True

                    parsedline.append("ADD")

                case "-=":
                    if not getvarflag:
                        return f"ERR AT LINE {uncookedline + 1}, WORD {wordindex + 1}: MISPLACED MINUS EQUAL SIGN"
                    parsedline[-1] -= nextword
                    calcflag = True
                    word_is_defined = True

                case "out":
                    consoleflag = True
                    word_is_defined = True

                    parsedline.append(word)

            if not word_is_defined:
                throwerr(error_info, "UNDEFINED WORD")

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

with open(f"{argv[1]}flhbytecode.flhb", "w") as result:
    result.write(str(file))
