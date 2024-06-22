#!/usr/bin/env python
""" A simple script that lists all my aliases that I have made in my terminal

I kept forgetting the many aliases that I make, so I made a script to list them out

"""

import os

__author___ = "Austin Greer"
__maintainer___ = "Austin Greer"
__email__ = "greer.austin1409@gmail.com"

if __name__ == '__main__':
    
    shellPath = os.getenv("PATH_TO_SHELL_PROFILE") 
    f = open(shellPath)

    listOfAliases = list()
    for line in f:
        if "alias " in line:
            
            firstSplit = line.split("alias ")
            secondSplit = firstSplit[1].split("=")
            
            listOfAliases.append(secondSplit[0])

    print("\n")
    print("\x1B[4mHere are your Alises:\x1B[0m") # This wizard shit is ANSI Escape Sequence
    for alias in listOfAliases:
        print("       " + alias)
            
    print("\n")
            
 