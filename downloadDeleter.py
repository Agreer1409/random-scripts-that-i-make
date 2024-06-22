#!/usr/bin/env python
""" Literally just clears my downloads folder.

You might be wondering "Why does he have a python script that clears a downloads folder?". 
The answer is simple. Why not? I was bored one day...

"""

import os
import send2trash

__author___ = "Austin Greer"
__maintainer___ = "Austin Greer"
__email__ = "greer.austin1409@gmail.com"


if __name__ == "__main__":

    downloadsPath = os.getenv('PATH_TO_DOWNLOADS_FOLDER')
    itemsToDownload = os.listdir(downloadsPath)

    if itemsToDownload == [] or len(itemsToDownload) == 0:
        print('\n')
        print('!~! There are no items to delete in the folder !~!')
        print('\n')
        exit()


    print("\nSending Items to Trash...")

    for item in itemsToDownload:
        send2trash.send2trash(downloadsPath + item)
    
    print("\nSuccess! All items moved to Trash!\n")
