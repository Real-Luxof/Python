from sys import argv as param

def findoption(params, opt):
    for option in params:
        if opt in option: return option.split(opt)[1]
    return False

if len(param) > 1:
    with open(param[1], "r") as file:
        data = file.read()
        data = data.split()

    decryptiontable = {
        "You": "1",
        "HaG!": "2",
        "i": "3",
        "NeVeR": "4",
        "SHouLD": "5",
        "HaVe": "6",
        "TrUsTEd": "7",
        "YOu.": "8",
        "Go": "9",
        "kilL": "!",
        "YourSELF": "@",
        "RIghT": "#",
        "noW!": "$",
        "WhY": "%",
        "WoulD": "^",
        "yOU": "&",
        "dO": "*",
        "ThiS": "(",
        "to": ")",
        "Me?": "a",
        "AfTeR": "b",
        "EvErYtHiNg": "c",
        "wE": "d",
        "hAvE": "e",
        "bEeN": "f",
        "tHrOuGh": "g",
        "ToGeThEr?": "h",
        "tHiS!!": "i",
        "is!!": "j",
        "whAT!!": "k",
        "yoU!!": "l",
        "giVE!!": "m",
        "back!!": "n",
        "TO!!": "o",
        "ME!!": "p",
        "you": "q",
        "uNgraTEFUl": "r",
        "IdIOtiC": "s",
        "rEtArD?!": "t",
        "?!?!?!": "u",
        "?!?!?!?!": "v",
        "?!?!?!?!?!": "w",
        "?!?!?!?!?!?!": "x",
        "?!?!?!?!?!?!?!": "y",
        "?!?!?!?!?!?!?!?!": "z",
        "iomg": "A",
        "wentomg": "B",
        "toomg": "C",
        "spaceomg": "D",
        "andomg": "E",
        "ateomg": "F",
        "aomg": "G",
        "hotdogomg": "H",
        "thereomg": "I",
        "itomg": "J",
        "wasomg": "K",
        "veryomg": "L",
        "refreshingomg": "M",
        "andomgomg": "N",
        "juicyomg": "O",
        "flavorfulomg": "P",
        "mouthwateringomg": "Q",
        "punchomg": "R",
        "sharpnessomg": "S",
        "unbreakingomg": "T",
        "mendingomg": "U",
        "protectionomg": "V",
        "thornsomg": "W",
        "infinityomg": "X",
        "biryaniomg": "Y",
        "ketchupomg": "Z",
        "kmsomg": "0",
        "OMGOMGOMG": " ",
        "thisissuchacertifiedkysmoment": "\n",
        "poggers": "\\n",
        "HOLYSHIT": ",",
        "IJUSTSHATMYPANTS!": ".",
        "^%@S": "<",
        "S@%^": ">",
        "youhonest?": "/",
        "nahimlyin": "?",
        "WINGsdIngS": ";",
        "nEvRkAlI!11!!": ":",
        "holyshitisthata": "'",
        "Bee$ecHuRgER": '"',
        "sIncEwheN": "[",
        "dIdU": "]",
        "waNNa": "{",
        "dIAEEE?": "}",
        "h0lym0ly": "-",
        "BASED!": "_",
        "based?": "=",
        "isitreallybasedthough?": "+",
        "noitsnotbased": "\\",
        "mostdefinitelybased!": "|",
        "whatdoItYPEAAAAA": "`",
        "IndustrialRevolutionAndItsConsequencesHaveBeenADisasterForTheHumanRace": "~",
    }
    cuttables = [["WHEREIS, REPEAT, WHEREIS", "TASKFORCETHIRTYFOUR? THEWORLD WONDERS."],["SINCE WHEN DID", "YOU EVER CARE?"],["isitreal lybasedtho ughh?" + "THEEI GHTWORL DWON DERS"],["heheheha PLANTSVSZOMBIES MAKESMEWET", "hohohohu PLANTSVSZOMBIES DOESSTUFFTOMEINTHEASS"],["IndustrialRevolution AndItsConsequences HaveBeenADisasterForTheHumanRace","IndustrialRevolution AndItsConsequences HaveBeenADisasterForTheHumanRace"]]
    if findoption(param,"password=") != False: password = findoption(param,"password="); password1 = password[slice(0,len(password)//2)]; password2 = password[slice(len(password)//2,len(password))]
    else: password1 = "ba"; password2 = "se"
    if findoption(param, "resultfile=") != False: resultfile = findoption(param,"resultfile=")
    else: resultfile = "DECRYPTIONRESULT.txt"
    output = ""
    
    if [data[0] + " " + data[1] + " " + data[2], data[-3] + " " + data[-2] + " " + data[-1]] in cuttables:
        if password1 == data[3] and password2 == data[-4]:
            del data[0]
            del data[0]
            del data[0]
            del data[0]
            del data[-1]
            del data[-1]
            del data[-1]
            del data[-1]
            for word in data:
                output += decryptiontable[word]

            with open(resultfile, "w+") as f:
                f.write(output)
        else:
            print("INCORRECT PASSWORD!")
    else:
        print("MANIPULATED AND/OR BAD FILE ENCOUNTERED!")
else:
    print("Usage: decrypt (required)file (optional)resultfile=(entername) (optional)password=(enterpassword)\nDon't forget the resultfile= and password=.")