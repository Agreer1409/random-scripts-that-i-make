import os
import send2trash


if __name__ == "__main__":

    itemsToDownload = os.listdir("/Users/greer/Downloads")

    if itemsToDownload == [] or len(itemsToDownload) == 0:
        print('\n')
        print('!~! There are no items to delete in the folder !~!')
        print('\n')
        exit()


    print("\nSending Items to Trash...")

    for item in itemsToDownload:
        send2trash.send2trash("/Users/greer/Downloads/" + item)
    
    print("\nSuccess! All items moved to Trash!\n")
