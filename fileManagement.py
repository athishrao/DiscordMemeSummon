import os
import threading

def getNames():
    files = []
    with open("memePages.txt", "r") as f:
        Lines = f.readlines()
        for line in Lines: 
            files.append(line.strip())
    return files

def storeImages():
    os.system("instagram-scraper -f memePages.txt --maximum 15")
    files = getNames()
    for randomPage in files:
        test = os.listdir(randomPage)
        for item in test:
            if item.endswith(".mp4"):
                os.remove(os.path.join(randomPage, item))
    threading.Timer(600.0, storeImages).start() # calls every 10 minutes
    print("New Memes Loaded!")

storeImages()