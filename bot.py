import discord
import random
import os
from os import listdir
from os.path import isfile, join

creds = []
with open("creds.txt", "r") as f:
    for line in f.readlines():
        creds.append(line.strip())
TOKEN = creds[0]
CHANNEL = int(creds[1])

client = discord.Client()
@client.event
async def on_message(message):
    if (message.content.find("Send a meme!") != -1):
        await message.channel.send("There you go")
        channel = client.get_channel(CHANNEL) 
        image = getImage()
        with open(image, 'rb') as fp:
            await channel.send(file=discord.File(fp, 'Meme.png'))
    if message.content.find("Stop!") != -1:
        await message.channel.send("Bye, guys! See you on the other side!")
        exit(0)

def getImage():
    files = getNames()
    print(files)
    randomPage = files[random.randint(0,len(files)-1)]
    print(randomPage)
    onlyfiles = [f for f in listdir(randomPage) if isfile(join(randomPage, f))]
    image = onlyfiles[random.randint(0,len(onlyfiles)-1)]
    image = randomPage+"/"+image
    return image    

def getNames():
    files = []
    with open("memePages.txt", "r") as f:
        Lines = f.readlines()
        for line in Lines: 
            files.append(line.strip())
    return files

client.run(TOKEN)