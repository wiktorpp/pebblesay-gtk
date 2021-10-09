#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################
#importing liblaries#
#####################

import argparse
from threading import Timer
from textwrap import wrap as textwrap
from os import _exit
import sys

############################
#declaring static variables#
############################

asciiart = [
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
maxWidth = 35

def generate(text, wrap=True, width=maxWidth, tailChar="\\"):
    #########################
    #parsing text (wrapping)#
    #########################

    #wrapping text
    if wrap: 
        textWrapped = []
        for i in text:
            textWrapped.extend(textwrap(i, width))
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

    return output

if __name__ == "__main__":
    ###############
    #fetching text#
    ###############
    text = " ".join(sys.argv[1:]).split("\\n")

    if text == [""]:
        #prinring usage message after a set time (I am so fucking smart :3)
        usageMsgTimer = Timer(0.1, 
            lambda: [print(
                "Usage: pebblesay [option]... [\033[4mmessage\033[0m]\n"
                "\n"
                "This program comes with \033[38;5;196mABSOLUTELY NO WARRANTY\033[39m, "
                "to the extent permitted byapplicable law."
            ), _exit(0)]
        )
        usageMsgTimer.start()
        #awaiting for text on stdin (peek() is blocking) and cancelling timer asap
        sys.stdin.buffer.peek(1)
        usageMsgTimer.cancel()
        text = stdin.read().splitlines()

    print("\n".join(generate(text)))