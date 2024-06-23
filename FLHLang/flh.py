"""The official Interpreter for FeelsLikeHellLang. The name is totally not a representation of what I feel when writing this code.

Btw, built in Python. Seethe."""

import math
# Imports and Arguments
from sys import argv
import typing
from ast import literal_eval
if len(argv) < 2 or len(argv) > 2: print("Usage: flh (filename)")

# Variables
vars: dict = {}
# Isn't really a list, just has variable names and their types.
vars_list: dict = {} # Used for the parser-lexer-compiler to figure shit out.
keywords: list = ["var", "out"]
operators: list = ["+", "-", "%", "/", "*", "^"]
varsetoperators: list = ["=", "+=", "-="]

# Functions
def throwerr(error_info: tuple[str, int, int], errmessage: str) -> None:
    """Throws an error to the user.

    Args:
        error_info (tuple): Info about the error.
        [0] = path to file.
        [1] = line index.
        [2] = word index.
        errmessage (str): The error message to throw.
    """
    path = error_info[0]
    line_index = error_info[1]
    word_index = error_info[2]
    print(f"{path}:{line_index + 1}:WORD {word_index + 1}: {errmessage}")
    print(f"{path}: ERR AT LINE {line_index + 1}, WORD {word_index + 1}: {errmessage}")
    quit()


def throwerr_line(error_info: tuple[str, int], errmessage: str) -> None:
    """Throws an error to the user.

    Args:
        error_info (tuple): Info about the error.
        [0] = path to file.
        [1] = line index.
        errmessage (str): The error message to throw.
    """
    path = error_info[0]
    line_index = error_info[1]
    print(f"{path}:{line_index + 1}: {errmessage}")
    print(f"{path}: ERR AT LINE {line_index + 1}: {errmessage}")
    quit()


def throwerr_letter(error_info: tuple[str, int, int], errmessage: str) -> None:
    """Throws an error to the user.

    Args:
        error_info (tuple[str, int, int]): Info about the error.
        [0] = path to file.
        [1] = line index.
        [2] = line index.
        errmessage (str): The error message to throw.
    """
    path = error_info[0]
    line_index = error_info[1]
    letter_index = error_info[2]
    print(f"{path}:{line_index + 1}:{letter_index}: {errmessage}")
    print(f"{path}: ERR AT LINE {line_index}, LETTER {letter_index + 1}: {errmessage}")
    quit()


def notoutofbounds(list: list, index: int) -> bool:
    """Checks if an index is out of bounds of a list.

    Args:
        list (list): The list to check.
        index (int): The index to check.

    Returns:
        bool: True if the index is not out of bounds, False otherwise.
    """
    if index < 0:
        return False
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


def give_internal_type(variable: str) -> str:
    """Gives the internal FLHLang type of {variable} if {variable} is in fact a variable, it will give the type of that variable.

    Args:
        variable (str): The string to check.

    Returns:
        str: The internal FLHLang type of {variable}.
    """
    try:
        return vars_list[variable]
    except(KeyError):
        pass
    
    if isint(variable): return "INTEGER"
    elif variable.startswith("[") and variable.endswith("]"): return "LIST"
    elif variable.startswith("(") and variable.endswith(")"): return "TUPLE"
    else: return "STRING"


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


def take_type(variable: str) -> typing.Any:
    """Returns the variable's type or removes the string representation.

    Args:
        variable (str): The string to be checked.

    Returns: Read the summary.
    """
    try:
        return vars_list[variable]
    except(KeyError):
        return givetype(variable)


#def convert_to_str(type: typing.Any) -> str:
#    """Returns the type name (e.g. list) to a string representation. (e.g. "list")
#
#    Args:
#        type (Any): the type to convert. (e.g. int)
#
#    Returns:
#        str: The string representation. (e.g. "int")
#    """
#    match type:
#        case int:
            


# Don't touch this. It just works.
def console_parse(error_inf: tuple[str, int], line: list[str]) -> None:
    """
    Performs console commands.
    out functions like print().
    in functions like input().
    
    Example (in FLHLang):
        out("Hello, World!")
        in("Say Hi! > ")
    """
    # if you can't understand this code i am not responsible to explain it to you.
    # yep it's totally not cuz i don't wanna climb the mental walls or do the gymanstics
    # to figure it out all over again
    
    # If it's not clear what it does even to me, I have to take a break since the brain 
    # fatigue has caught up to me.
    # Das ist mein philosophy.
    
    # Initalization of variables
    global vars_list
    parsed_line = []
    in_par = ""
    strs = []
    in_str = False
    addflag = False
    prob_var = False
    
    error_info = list(error_inf)
    error_info.append(3)
    
    
    # This is needed to do some shenanigans
    next_letters = []
    for letter in line:
        next_letters.append(letter)
    del next_letters[0]
    del next_letters[0]
    del next_letters[0]
    del next_letters[0]
    
    if line.startswith("out"):
        
        if not line.startswith("out("):
            throwerr_letter(tuple(error_info), "MISSING PARENTHESIS AFTER 'OUT'.")
        
        if not line.endswith(")"):
            error_info[-1] = -1
            throwerr_letter(tuple(error_info), "PARENTHESIS NOT CLOSED.")
        
        for letter_index in range(4, len(line)):
            letter = line[letter_index]
            error_now = True # this is used SPECIFICALLY for +
            #add_var = False # this is also used SPECIFICALLY for +
            # kmn kmn kmn kmn kmn kmn kmn kmn kmn kmn kmn
            error_info[-1] += 1
            del next_letters[0]
            
            match letter:
                case ")":
                    if in_str:
                        throwerr_letter(tuple(error_info), "PARENTHESIS CLOSED BEFORE STRING.")
                    
                    for string in strs:
                        in_par += string
                    
                    # TODO: finish this
            
                case "\"":
                    if in_str:
                        in_str = False
                        parsed_line.append(strs[-1])
                    else:
                        strs.append("")
                        in_str = True
                
                case _:
                    if in_str:
                        strs[-1] += letter
                    
                    elif isint(letter):
                        strs.append(f"int {letter}")
                    
                    elif letter == "+":
                        addflag = True
                        for next_letter in next_letters:
                            
                            if next_letter == "+":
                                throwerr_letter(error_info, "ADDING LITERALLY NOTHING AND THEN ADDING SOMETHING ELSE, WTF?")
                            
                            elif next_letter == "\"":
                                error_now = False
                                break
                            
                            elif isint(next_letter):
                                error_now = False
                                break
                            
                            elif next_letter == ")":
                                throwerr_letter(error_info, "PARENTHESIS CLOSED BEFORE ADDING ANYTHING.")
                            
                            elif next_letter != " ":
                                error_now = False
                                #add_var = True
                                break
                        
                        if error_now:
                            throwerr_letter(error_info, "ADDING LITERALLY NOTHING.")
                        
                        # commenting the add_var parts out fixed a problem wtf
                        # this code is a black box and i don't wanna bother putting all of it in my mind
                        #if add_var:
                        #    strs.append("getvar ")
                    
                    elif addflag and letter != " ":
                        strs[-1] += letter
                    
                    # this part was made so out(foo) does not return ['']
                    elif not in_str:
                        # probably a variable
                        if not prob_var:
                            strs.append("getvar ")
                            prob_var = True
                        
                        if letter != " ":
                            strs[-1] += letter
                        else:
                            prob_var = False
    
    for string_index in range(len(strs)):
        string = strs[string_index]
        string_without_getvar = string.removeprefix("getvar ")
        
        if not string.startswith("getvar "):
            continue
        
        if not string_without_getvar in vars_list.keys():
            throwerr_line(error_inf, f"VARIABLE {string_without_getvar} MISSING.")
    
    return ["out"] + strs

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

# Completes the whole olympics and gets a gold medal, called a cyclist.
def parsefile(pathtofile):
    # Get some globals.
    global vars_list
    global keywords
    global operators
    global varsetoperators
    
    # Stuff to do with the file.
    f = open(pathtofile, "r")
    file = f.readlines()
    f.close()
    
    parsedfile = []
    
    # Some flags.
    setvarflag = False
    final_setvarflag = False
    getvarflag = False
    calcflag = False
    consoleflag = False
    
    for uncookedlineindex in range(len(file)):
        uncookedline = file[uncookedlineindex].removesuffix("\n")
        # LET HIM COOK :fire:
        cookedline = uncookedline.split(" ")
        parsedline = []
        
        if uncookedline.startswith("out") or uncookedline.startswith("in"):
            parsedline = console_parse((pathtofile, uncookedlineindex), uncookedline.removesuffix("\n"))
            parsedfile.append(parsedline)
            continue
        
        for wordindex in range(len(cookedline)):
            # Initialize some variables -
            
            # Get the words
            word = cookedline[wordindex]
            word_is_defined = False
            
            if notoutofbounds(cookedline, wordindex - 1):
                prev_word = cookedline[wordindex - 1]
            else:
                prev_word = None
            
            if notoutofbounds(cookedline, wordindex + 1):
                nextword = cookedline[wordindex + 1]
            else:
                nextword = None
            
            if notoutofbounds(cookedline, wordindex + 2):
                nextnextword = cookedline[wordindex + 2]
            else:
                nextnextword = None
            
            # Get some error info in case there's an error.
            error_info = (pathtofile, uncookedlineindex, wordindex)
            error_info_nextword = (pathtofile, uncookedlineindex, wordindex + 1)
            
            match word:
                case "var":
                    if nextword in vars_list and nextnextword != "=":
                        getvarflag = True
                        parsedline.append("getvar")
                        continue
                    
                    setvarflag = True
                    parsedline.append("getvar")
                
                case "=":
                    if not setvarflag:
                        throwerr(error_info, "MISPLACED EQUAL SIGN.")
                    
                    # Disable setvarflag as its purpose has been fulfilled.
                    setvarflag = False
                    final_setvarflag = True
                
                case "+=":
                    if setvarflag or not getvarflag:
                        # You can't just "var unknown_variable += value" thus setvarflag is not allowed.
                        throwerr(error_info, "MISPLACED PLUS EQUAL SIGN.")
                    
                    type_of_var = give_internal_type(prev_word)
                    type_of_nextword = give_internal_type(nextword)
                    
                    if type_of_var != type_of_nextword:
                        throwerr(error_info, f"CANNOT ADD {type_of_var} AND {type_of_nextword}.")
                    
                    if not nextnextword in operators:
                        parsedline.append("ADD")
                    else:
                        parsedline.append("ADD_CALC_FIRST")
                
                case "-=":
                    if setvarflag or not getvarflag:
                        # You can't just "var unknown_variable += value" thus setvarflag is not allowed.
                        throwerr(error_info, "MISPLACED PLUS EQUAL SIGN.")
                    
                    type_of_var = give_internal_type(prev_word)
                    type_of_nextword = give_internal_type(nextword)
                    
                    if type_of_var != type_of_nextword:
                        throwerr(error_info, f"CANNOT SUBTRACT {type_of_nextword} FROM {type_of_var}.")
                    
                    if not nextnextword in operators:
                        parsedline.append("SUB")
                    else:
                        parsedline.append("SUB_CALC_FIRST")
                
                case "+":
                    if setvarflag or not getvarflag:
                        # You can't just "var unknown_variable += value" thus setvarflag is not allowed.
                        throwerr(error_info, "MISPLACED PLUS EQUAL SIGN.")
                    
                    type_of_var = give_internal_type(prev_word)
                    type_of_nextword = give_internal_type(nextword)
                    
                    if type_of_var != type_of_nextword:
                        throwerr(error_info, f"CANNOT ADD {type_of_var} AND {type_of_nextword}.")
                    
                    parsedline.append("ADD")
                    
                
                # In case we don't know what to do with it, look at some flags.
                case _:
                    
                    if setvarflag:
                        parsedline.append(word)
                        vars_list[word] = give_internal_type(nextnextword)
                        # Don't disable setvarflag as it is needed further on.
                        word_is_defined = True
                    
                    elif final_setvarflag:
                        parsedline.append(word)
                        # Disable final_setvarflag as it is no longer needed.
                        final_setvarflag = False
                        word_is_defined = True
                    
                    elif getvarflag:
                        parsedline.append(word)
                        # getvarflag is still needed, so don't disable it.
                        word_is_defined = True
                    
                    if not word_is_defined:
                        throwerr(error_info, "UNDEFINED WORD.")
        

        parsedfile.append(parsedline)
    
    return parsedfile

def interpret(parsedfile):
    global vars
    global keywords

    for lineindex in range(len(parsedfile)):
        for wordindex in range(lineindex):
            # Declare and get Variables
            pass

if __name__ == "__main__":
    file = parsefile(argv[1])

    # flb stands for Feels Like Bytecode
    # for some reason i'm really proud of myself for that
    file_name = argv[1].removesuffix(".flh").split("\\")[-1]
    with open(f"FeelsLikeBytecode\\{file_name}.flb", "w") as result:
        result.write(str(file))
