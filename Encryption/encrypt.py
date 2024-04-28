from sys import argv as param
from random import choice

def findoption(params, opt):
    for option in params:
        if opt in option: return option.split(opt)[1]
    return False

if len(param) > 1:
    with open(param[1], "r") as file:
        data = file.read()
        
    encryptiontable = {
        "1": "You ",
        "2": "HaG! ",
        "3": "i ",
        "4": "NeVeR ",
        "5": "SHouLD ",
        "6": "HaVe ",
        "7": "TrUsTEd ",
        "8": "YOu. ",
        "9": "Go ",
        "!": "kilL ",
        "@": "YourSELF ",
        "#": "RIghT ",
        "$": "noW! ",
        "%": "WhY ",
        "^": "WoulD ",
        "&": "yOU ",
        "*": "dO ",
        "(": "ThiS ",
        ")": "to ",
        "a": "Me? ",
        "b": "AfTeR ",
        "c": "EvErYtHiNg ",
        "d": "wE ",
        "e": "hAvE ",
        "f": "bEeN ",
        "g": "tHrOuGh ",
        "h": "ToGeThEr? ",
        "i": "tHiS!! ",
        "j": "is!! ",
        "k": "whAT!! ",
        "l": "yoU!! ",
        "m": "giVE!! ",
        "n": "back!! ",
        "o": "TO!! ",
        "p": "ME!! ",
        "q": "you ",
        "r": "uNgraTEFUl ",
        "s": "IdIOtiC ",
        "t": "rEtArD?! ",
        "u": "?!?!?! ",
        "v": "?!?!?!?! ",
        "w": "?!?!?!?!?! ",
        "x": "?!?!?!?!?!?! ",
        "y": "?!?!?!?!?!?!?! ",
        "z": "?!?!?!?!?!?!?!?! ",
        "A": "iomg ",
        "B": "wentomg ",
        "C": "toomg ",
        "D": "spaceomg ",
        "E": "andomg ",
        "F": "ateomg ",
        "G": "aomg ",
        "H": "hotdogomg ",
        "I": "thereomg ",
        "J": "itomg ",
        "K": "wasomg ",
        "L": "veryomg ",
        "M": "refreshingomg ",
        "N": "andomgomg ",
        "O": "juicyomg ",
        "P": "flavorfulomg ",
        "Q": "mouthwateringomg ",
        "R": "punchomg ",
        "S": "sharpnessomg ",
        "T": "unbreakingomg ",
        "U": "mendingomg ",
        "V": "protectionomg ",
        "W": "thornsomg ",
        "X": "infinityomg ",
        "Y": "biryaniomg ",
        "Z": "ketchupomg ",
        "0": "kmsomg ",
        " ": "OMGOMGOMG ",
        "\n": "thisissuchacertifiedkysmoment ",
        "\\n": "poggers ",
        ",": "HOLYSHIT ",
        ".": "IJUSTSHATMYPANTS! ",
        "<": "^%@S ",
        ">": "S@%^ ",
        "/": "youhonest? ",
        "?": "nahimlyin ",
        ";": "WINGsdIngS ",
        ":": "nEvRkAlI!11!! ",
        "'": "holyshitisthata ",
        '"': "Bee$ecHuRgER ",
        "[": "sIncEwheN ",
        "]": "dIdU ",
        "{": "waNNa ",
        "}": "dIAEEE? ",
        "-": "h0lym0ly ",
        "_": "BASED! ",
        "=": "based? ",
        "+": "isitreallybasedthough? ",
        "\\": "noitsnotbased ",
        "|": "mostdefinitelybased! ",
        "`": "whatdoItYPEAAAAA ",
        "~": "IndustrialRevolutionAndItsConsequencesHaveBeenADisasterForTheHumanRace "
    }
    cuttables = [["WHEREIS, REPEAT, WHEREIS", "TASKFORCETHIRTYFOUR? THEWORLD WONDERS."],["SINCE WHEN DID", "YOU EVER CARE?"],["isitreal lybasedtho ughh?" + "THEEI GHTWORL DWON DERS"],["heheheha PLANTSVSZOMBIES MAKESMEWET", "hohohohu PLANTSVSZOMBIES DOESSTUFFTOMEINTHEASS"],["IndustrialRevolution AndItsConsequences HaveBeenADisasterForTheHumanRace","IndustrialRevolution AndItsConsequences HaveBeenADisasterForTheHumanRace"]]
    if findoption(param,"password=") != False: password = findoption(param,"password="); password1 = password[slice(0,len(password)//2)]; password2 = password[slice(len(password)//2,len(password))]
    else: password1 = "ba"; password2 = "se"
    if findoption(param, "resultfile=") != False: resultfile = findoption(param,"resultfile=")
    else: resultfile = "ENCRYPTIONRESULT.txt"
    output = ""
    for char in data:
        output += encryptiontable[char]

    with open(resultfile, "w+") as f:
        cuttable = choice(cuttables)
        f.write(cuttable[0] + " " + password1 + " " + output + " " + password2 + " " + cuttable[1])
else:
    print("Usage: encrypt (required)file (optional)resultfile=(entername) (optional)password=(enterpassword)\nDon't forget the resultfile= and password=.")