#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################
#importing liblaries#
#####################

import argparse
from threading import Timer
from textwrap import wrap
from os import _exit

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
        "pebblesay [option]... [\033[4mmessage\033[0m]",
    description=None,
    epilog=
        "This program comes with \033[38;5;196mABSOLUTELY NO WARRANTY\033[39m, "
        "to the extent permitted byapplicable law.",
)
parser.add_argument("-t", "--think", action="store_true", 
    help="print a thought bubble instead of a speech bubble"
)
parser.add_argument("-m", "--mods", nargs="*", type=str, metavar="MOD")
parser.add_argument("-w", "--width", default=maxWidth, type=int, 
    help=f"set the width for word wrapping (default: {maxWidth})"
)
parser.add_argument("-n", "--nowrap", action="store_true", 
    help="disable line wrapping"
)
parser.add_argument("-p", "--pipe", action="store_true", 
    help="force reading from STDIN"
)
parser.add_argument("message", nargs="*", type=str, 
    help="message to be displayed in the speech bubble"
)

args = parser.parse_args()
text = " ".join(args.message).split("\\n")

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
            print(f"Error: Invalid mod name {modName}.")

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
textWidth = max(len(i) for i in text)
textHeight = len(text)

##########
#printing#
##########
output = []

#generating top line
output.append(f" {'_' * (textWidth + 2)}   ")

#one line of text
if textHeight == 1:
    output.append(f"< {text[0]} >  ")

#multiple lines of text
else:
    for i, line in enumerate(text):
        if i == 0:
            output.append(f"/ {line.ljust(textWidth)} \\  ")
        elif textHeight - i == 1:
            output.append(f"\\ {line.ljust(textWidth)} /  ")
        else:
            output.append(f"│ {line.ljust(textWidth)} │  ")

spacing = " " * textWidth

#creating bottom line and the tail
tailChar = "\\" if not args.think else "o"
output.append(f" {'¯' * (textWidth + 2)} {tailChar} ")
output.append(f"{spacing}     {tailChar}")

output = [f"{bubbleLine}{asciiartLine}" for bubbleLine, asciiartLine in 
    zip(
        output, 
        ["" for _ in range(textHeight + 3 - 4)] + asciiart[:4]
    )
]

#appending the rest of asciiart
for line in asciiart[4:]:
    output.append(f"{spacing}{line}")

print("\n".join(output))