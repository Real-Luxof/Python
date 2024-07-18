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
vars_list: dict = {} # Used for the parser to figure type shit out.

keywords: list = ["var", "out"] # puny
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


def shunting_yard_algorithm(equation_infix: str) -> str:
    """Applies the shunting yard algorithm to translate an input into reverse polish notation.

    Args:
        equation_infix (str): The equation, should be in infix notation.

    Returns:
        str: The equation as expressed in postfix (reverse polish) notation.
    """
    # yarrr, i hate parenthesis. FUCK parenthesis.
    equation = equation_infix.split(" ")
    operators = ["+", "-", "%", "/", "*", "^"]
    # 0 = left
    # 1 = right
    assoc_table = {
        "^": 1,
        "*": 0,
        "%": 0,
        "/": 0,
        "+": 0,
        "-": 0
    }
    prec_table = {
        "^": 4,
        "*": 3,
        "%": 3,
        "/": 3,
        "+": 2,
        "-": 2
    }
    op_1 = None
    op_2 = None
    output_queue = []
    operator_stack = []
    
    for token in equation:
        if isint(token):
            output_queue.append(token)
        
        elif token in operators:
            if len(operator_stack) == 0:
                operator_stack.append(token)
                continue
            
            op_1 = token
            while True:
                if len(operator_stack) == 0:
                    break
                
                op_2 = operator_stack[-1]
                
                if op_2 == "(":
                    break
                
                if (
                    (prec_table[op_2] > prec_table[op_1])
                    or 
                    (prec_table[op_2] == prec_table[op_1] and assoc_table[op_2] == 0)
                ):
                    output_queue.append(operator_stack.pop())
                else:
                    break
                
            operator_stack.append(token)
        
        elif token == "(":
            operator_stack.append(token)
        
        elif token == ")":
            if len(operator_stack) == 0:
                ValueError("Parenthesis not even opened, what are you closing?")
            
            if "(" not in operator_stack:
                ValueError("Parenthesis not even opened, what are you closing?")
            
            for op_index in reversed(range(len(operator_stack))):
                if operator_stack[op_index] == "(":
                    operator_stack.pop(op_index)
                    break
                
                output_queue.append(operator_stack.pop(op_index))
    
    output_queue += list(reversed(operator_stack))
    
    return " ".join(output_queue)


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
    elif variable.startswith("["): return "LIST"
    elif variable.startswith("("): return "TUPLE"
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


def lex(text: str):
    # what it should do:
    # IN << 'it can lex this right? yeah okay "test" (muahaha "test2") "test3 "'
    # OUT >> [
        # ['it', 'can', 'lex', 'this', 'right?', 'yeah', 'okay'],
        # ['"', 'test', '"'],
        # ['(', 'muahaha', ['"', 'test2', '"'], ')']],
        # ['"', 'test3 ', '"']
    # ]
    #
    # IN << 'out("haiii :3")'
    # OUT >> [
        # ['out'],
        # ['(', ['"', 'haiii :3', '"'], ')']
    #]
    #
    # IN << 'var a = "HIGH QUALITY CHIC" + "KEN FOR SALE"'
    # OUT >> [
        # ['var', 'a', '='],
        # ['"', 'HIGH QUALITY CHIC', '"'],
        # ['+'],
        # ['"', 'KEN FOR SALE', '"']
    #]
    #
    # i don't know what happens if there's an unclosed parenthesis or something
    # but i'll leave that to the parser to find and freak out about lmao
    text_lines = text.split("\n")

    tokens: list[list[str]] = [[]] # this is for lines of tokens
    occupied: list[str] = [] # please dont ask idk how to express this
    buffer: list[str, list[str]] = [] # idk how to express this either
    previous_accessing_indexes = []
    current_accessing_index = tokens[-1] # i pray to god this is a pointer and not a clone
    
    opening_and_closing_triggers = {
        '"': '"',
        "(": ")",
        "[": "]",
        " ": " "
    }

    for letter in text:
        # THROUGH THE FIRE AND THE FLAMES
        # THROUGH THE FIRE AND THE FLAMES
        
        if letter == " ":
            if len(occupied) > 0:
                current_accessing_index.append()
            pass
        elif letter == occupied[-1]:
            current_accessing_index
        
        elif letter in opening_and_closing_triggers.keys():
            occupied.append(letter)
            current_accessing_index.append(letter)
            
            continue
        
        elif letter != " ":
            occupied.append(" ")
            current_accessing_index.append(letter)
            
            continue
        
        if letter == opening_and_closing_triggers[occupied[-1]]:
            del occupied[-1]
            current_accessing_index = previous_accessing_indexes.pop()
            current_accessing_index.append(letter)
            
            continue
        
        current_accessing_index


# nya. ich nii san nya, arigato.
# average 11:50 PM comment:

# 4th time people, how many more are left?
def parsefile(pathtofile):
    
    # Get globals (fun*)
    global vars_list
    global operators
    
    # Read le file.
    f = open(pathtofile, "r")
    file = f.read().split("\n")
    f.close()
    
    # AST (yay)
    # top layer has to be a list (nay)
    AST = []
    
    for unc_line_index in range(len(file)):
        # line stuff
        unc_line = file[unc_line_index]
        line = unc_line.split(" ")
        
        # temp ast to append to AST
        TEMP_AST = {}
        
        # need flags variables (fun*)
        var_name_set_flag = False
        var_val_set_flag = False
        
        for word_index in range(len(line)):
            # error info gathering
            word = line[word_index]
            error_info = (pathtofile, unc_line_index, word_index)
            
            match word:
                
                case "var":
                    var_name_set_flag = True
                    TEMP_AST["var"] = {}
                
                case "=":
                    if not var_val_set_flag:
                        throwerr(error_info, "MISPLACED EQUAL SIGN.")
                
                case _:
                    if var_name_set_flag:
                        
                        # set name :D
                        TEMP_AST["var"]["name"] = word
                        
                        # some flags
                        var_name_set_flag = False
                        var_val_set_flag = True
                        continue
                    
                    elif var_val_set_flag:
                        
                        # huzzah, value setting.
                        type_of_val = give_internal_type(word)
                        
                        if type_of_val == "INT":
                            TEMP_AST["var"]["val"] = int(word)
                        
                        # take it if it's a one word thing
                        # yeah strings are defined with double quotes here
                        # fuck the user if they use single quotes i guess
                        if word.startswith("\"") and word.endswith("\""):
                            # remove the double quotes
                            val = word.removeprefix("\"")
                            val = val.removesuffix("\"")
                            TEMP_AST["var"]["val"] = val
                            
                            var_val_set_flag = False
                            continue
                        
                        elif word_index == len(line):
                            if isint(word):
                                TEMP_AST["var"]["val"] = int(word)
                            
                            continue
                        
                        # what if it's not that simple?
                        # then embark with me on this journey of my mind only
                        # half analyzing what it sees with a for loop, new_error_info,
                        # and a chase for the last ending double quotes that might not
                        # even exist.
                        if not unc_line.endswith("\""):
                            throwerr(error_info, "STRING OPENED BUT NOT CLOSED.")
                        
                        # spaghetti code?
                        math = []
                        val = word.removeprefix("\"")
                        not_in_str = False
                        op_added = False
                        limit = len(line) - word_index
                        
                        for index in range(1, limit):
                            new_error_info = (pathtofile, unc_line_index, word_index + index)
                            
                            str_word = line[word_index + index] # lack of a better term in my mind
                            
                            if not_in_str:
                                if str_word in operators:
                                    if op_added:
                                        throwerr(new_error_info, "OPERATOR CHAIN.")
                                    elif index == limit:
                                        throwerr(new_error_info, "OPERATOR ADDED AT THE END OF THE LINE.")
                                    
                                    math += str_word
                                    op_added = True
                                
                                elif str_word.startswith("\""):
                                    if not op_added:
                                        throwerr(new_error_info, "NEW STRING OPENED WITH NO OPERATOR BEFOREHAND.")
                                    
                                    not_in_str = False
                                    val = str_word.removeprefix("\"")
                                    op_added = False
                                
                                elif isint(str_word):
                                    if not op_added:
                                        throwerr(new_error_info, "NEW INTEGER ADDED WITH NO OPERATOR BEFOREHAND.")
                                    
                                    if index == limit:
                                        break
                                    
                                    math += str_word
                            
                            elif str_word.endswith("\""):
                                val += str_word.removesuffix("\"")
                                
                                if index == limit:
                                    break
                                
                                math += val
                                val = ""
                                not_in_str = True
                            
                            
                            # "if math's not empty, stop the line" for scrubs
                            if not math:
                                break
                            
                            # time to sort out math :(
                            
                            # PEMDAS without the P
                            EMDAS = {
                                "^": 2,
                                "*": 1,
                                "/": 1,
                                "+": 0,
                                "-": 0
                            } 
                            
                            equation = {} # i have no idea how to explain this
                            
                            for op in EMDAS.keys():
                                if op not in math:
                                    del EMDAS[op]
                            
                            for step_index in range(len(math)):
                                step = math[step_index]
                                
                                if not notoutofbounds(step, "op"):
                                    continue
                                
                                op = step["op"]
                                highest_prio_op = EMDAS[list(EMDAS.keys())[0]]
                                
                                #if op
                            
                            for prio_step_index in range(len(EMDAS)):
                                prio_step = EMDAS[prio_step_index]
                                # no better word than prio_step in my mind rn
                                
                                for step_index in range(len(math)):
                                    step = math[step_index]
                                    
                                    if not notoutofbounds(step, "op"):
                                        continue
                                    
                                    operator = step["op"]
                                    
                                    if operator == prio_step:
                                        if not equation:
                                            equation = {
                                                prio_step: {}
                                            }
                                            continue
                                        
                                        deepest_point = list(equation.keys())
                                        
                                        #for i in range(len(EMDAS)):
                                            #if EMDAS[prio_step_index + 1]
                                        
        
        AST.append(TEMP_AST)


"""
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
                        # Don't disable final_setvarflag if it's still needed.
                        if word.endswith("\""):
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
"""
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
