#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################
#importing liblaries#
#####################

from sys import *
from os import *
from threading import Timer
from textwrap import wrap

############################
#declaring static variables#
############################

baseAsciiart = [
                      "     /|_   ___/|",
                      "    / __\\_/    |",
                      "   | /     \\   >",
                      "  / | Ó  °_ | /",
                "        | \\ ░ W ░/  |",
                "         \\_ |   _| /",
                "           < \\// -\\\  ___",
                "         /  /  _ --|\\/   \\",
                "         | /  / --/ |    /",
                "         \\   / \\     >  /",
                "   __     \\/__/_  / \\_  \\",
                "  O   \\  / /O O \\     \\  \\",
                "   O   \\/  °(_)°|      \\  |",
                "    \\   \\   \\   |      |  |",
                "     \\   \\   |   \\     | /",
                "      \\      |    |   /",
                "       \\_____\\___/___/",
]
mods = {
    "imgNoColor" : [
                          "     /|_   ___/|",
                          "    / __\\_/    |",
                          "   | /     \\   >",
                          "  / | Ó  °_ | /",
                    "        | \\ ░ W ░/  |",
                    "         \\_ |   _| /",
                    "           < \\// -\\\  ___",
                    "         /  /  _ --|\\/   \\",
                    "         | /  / --/ |    /",
                    "         \\   / \\     >  /",
                    "   __     \\/__/_  / \\_  \\",
                    "  O   \\  / /O O \\     \\  \\",
                    "   O   \\/  °(_)°|      \\  |",
                    "    \\   \\   \\   |      |  |",
                    "     \\   \\   |   \\     | /",
                    "      \\      |    |   /",
                    "nocolor\\_____\\___/___/(todo)"
    ],
    "uwu" : [
             "*",
             "*",
             "*",
             "  / | U   U | /"
    ],
    "ono" : [
                   "*",
                   "*",
                   "*",
                   "  / | O   O | /",
             "        | \\ ░ n ░/  |"
    ],
    "x3" : [
                   "*",
                   "*",
                   "*",
                   "  / | >   < | /",
             "        | \\ ░ W ░/  |"
    ]
}
maxWidth = 35

#################
#setting options#
#################

#determining options
forcePipe = think = wrapping = force = colorDisabled = False
nextIterWidth = nextIterMod = False
isTextInParameters = False
textOffset = 1
modsEnabled = []
for i in argv[1:]:

    #setting width
    if nextIterWidth:
        if i == "0":
            print("Error: Width can't be set to 0.")
            continue
        try:
            width = int(i)
        except:
            print("Error: Width value incorrect.")
            continue
        wrapping = True

        nextIterWidth = False
        textOffset += 1
        continue

    if nextIterMod:
        modsEnabled.extend(i.split("+"))
        nextIterMod = False
        textOffset += 1
        continue

    #stopping at the end of options
    if not i.startswith("-") and not nextIterWidth:
        isTextInParameters = True
        break

    if "p" in i:
        forcePipe = True
    if "t" in i:
        think = True
    if "n" in i:
        wrapping = True
    if "f" in i:
        force = True
    if "c" in i:
        modsEnabled.append("imgNoColor")

    if "w" in i:
        nextIterWidth = True
    if "m" in i:
        nextIterMod = True

    textOffset += 1

#setting width to max if not specified
try: width
except:
    width = maxWidth

#turning on text wrapping if text supplied as argument
if isTextInParameters and not "\\n" in " ".join(argv[textOffset:]):
    wrapping = True

#configuring asciiart
asciiart = baseAsciiart
try: 
    modsEnabled
except:
    pass
else:
    for modName in modsEnabled:
        mod = mods.get(modName)
        lineIndex = 0
        if mod != None:
            for line in mod:
                if line != "*":
                    #replacing line with the mod
                    asciiart[lineIndex] = line
                lineIndex +=1
        else:
            print("Error: Invalid mod name " + modName + ".")

###############
#fetching text#
###############

#fetching text from arguments
if isTextInParameters:
    text = " ".join(argv[textOffset:]).split("\\n")

#if no text supplied in arguments
def usageMsg():
    print("Usage: pebblesay [option]... [-m \033[4mmods\033[0m] " + \
        "[\033[4mmessage\033[0m]")
    print("This program comes with " + chr(0x1B) + "[38;5;196mABSOLUTELY NO " \
        + "WARRANTY" + chr(0x1B) + "[39m, to the extent permitted by "\
        + "\napplicable law.")
    print("Options:")
    print("  -t -> think")
    print("  -m -> specify what modifications to apply to the base asciiart " \
        + "(seperated by \n" \
          "        a plus sign starting with the most invasive ones first)")
    print("  -n -> toggle word wrapping")
    print("  -w [number] -> set the width for word wrapping")
    #print("  -f force")
    print("  -c -> disable color (todo)")
    print("  -p -> force reading from pipe")
    print("Usage examples:")
    print("  -> pebblesay XD")
    print("  -> figlet XD | pebblesay")
    print("  -> pebblesay -m uwu uwu")
    print("  -> cat file.txt | pebblesay -n")
    print('  -> pebblesay "Hi, \\nhow are you?"')
    _exit(0)

if not isTextInParameters and not forcePipe:
    #prinring usage message after a set time (I am so fucking smart :3)
    usageMsgTimer = Timer(0.1, usageMsg)
    usageMsgTimer.start()
    #awaiting for text on stdin (peek() is blocking) and cancelling timer asap
    stdin.buffer.peek(1)
    usageMsgTimer.cancel()
    text = stdin.read().splitlines()

#-p specified
if forcePipe:
    text = stdin.read().splitlines()

#########################
#parsing text (wrapping)#
#########################

#checking if text supplied
if not force:
    if (len(text) == 1 and (text[0] == "" or text[0] == " ")) or len(text) == 0:
        print("Error: No text Supplied.")
        _exit(1)

#wrapping text
if wrapping:
    textTmp = text
    text = []
    for i in textTmp:
        text.extend(wrap(i, width))

#calculating width
width = max(len(i) for i in text)

##########
#printing#
##########(finally)
output = ""

#generating top line
output += " _"
for i in range(0, width):
    output += '_'
output += "_"

#one line of text
if len(text) == 1:
    output += f"   {asciiart[0]}\n"
    output += f"< {text[0]} >  {asciiart[1]}\n"

#multiple lines of text
elif len(text) > 1:
    output += "\n"
    for i in range(0, len(text)):
        if i == 0:
            output += f"/ {text[0].ljust(width)} \\  "
        elif len(text) - i == 1:
            output += f"\\ {text[i].ljust(width)} /  "
        else:
            output += f"│ {text[i].ljust(width)} │  "

        #printing asciiart
        if len(text) - i == 2:
            output += asciiart[0]
        elif len(text) - i == 1:
            output += asciiart[1]

        output += "\n"

spacing = " " * width

#creating bottom line
output += " ¯"
for i in range(0, width):
    output += '¯'
output += "¯ "
if not think:
    output += f"\\ {asciiart[2]}\n"
    output += spacing + "     \\{asciiart[3]}\n"
else:
    output += "o {}\n".format(asciiart[2])
    output += spacing + "     o{asciiart[3]}\n"

#appending the rest of asciiart
for i in range(4, len(asciiart)):
    output += f"{spacing}{asciiart[i]}\n"

stdout.write(output)