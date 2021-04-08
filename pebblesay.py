#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################
#importing liblaries#
#####################

from sys import *
from os import *
import argparse
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

# Create the parser (should have used that from the begining)
parser = argparse.ArgumentParser(
    prog="nishisay",
    usage=
        "Usage: pebblesay [option]... [\033[4mmessage\033[0m]",
    description=
        "This program comes with \033[38;5;196mABSOLUTELY NO WARRANTY\033[39m, to the extent permitted by applicable law.",
)
parser.add_argument("-t", "--think", action="store_true")
parser.add_argument("-m", "--mods", nargs="*", type=str)
parser.add_argument("-w", "--width", default=maxWidth, type=int, help="set the width for word wrapping")
parser.add_argument("-n", "--nowrap", action="store_true")
parser.add_argument("-p", "--pipe", action="store_true", help="force reading from pipe")
parser.add_argument("text", nargs="*", type=str)
args = parser.parse_args()

text = " ".join(args.text).split("\\n")

#turning on text wrapping if text supplied as argument
if text=="" and not args.nowrap:
    wrapping = True

#configuring asciiart
asciiart = baseAsciiart
if args.mods != None:
    for modName in args.mods:
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
if text == [""] and not args.pipe:
    #prinring usage message after a set time (I am so fucking smart :3)
    usageMsgTimer = Timer(0.1, 
        lambda: [parser.print_help(), _exit(0)]
    )
    usageMsgTimer.start()
    #awaiting for text on stdin (peek() is blocking) and cancelling timer asap
    stdin.buffer.peek(1)
    usageMsgTimer.cancel()
    text = stdin.read().splitlines()

#-p specified
elif args.pipe:
    text = stdin.read().splitlines()

#########################
#parsing text (wrapping)#
#########################

#wrapping text
if not args.nowrap: 
    textWrapped = []
    for i in text:
        textWrapped.extend(wrap(i, args.width))
text=textWrapped

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
if not args.think:
    output += f"\\ {asciiart[2]}\n"
    output += spacing + f"     \\{asciiart[3]}\n"
else:
    output += f"o {asciiart[2]}\n"
    output += spacing + f"     o{asciiart[3]}\n"

#appending the rest of asciiart
for i in range(4, len(asciiart)):
    output += f"{spacing}{asciiart[i]}\n"

stdout.write(output)