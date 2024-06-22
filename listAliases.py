import os

if __name__ == '__main__':
    
    f = open("/Users/greer/.zshrc")

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
            
 