# Random Meme Summoner

This is a snippet that creates a Discord Bot that summons a random meme from a random web OPEN instagram meme pages. The list of meme pages can be loaded onto the memePages.txt file.

### bot.py
```sh
$ python bot.py
```
Runnning the above would launch the bot and make it active for summoning.

### fileManagement.py 
```sh
$ nohup python fileManagement.py &
```
Would run the fileManagement code in the backgroud and would look for new content every 10 minutes. Removes mp4 files from the folders, if any.

### creds.txt
Create a file called cred.txt with the first line as the Token and the second line as the Channel number.

### memePages.txt
Add open meme pages delimited by newline character


### On Discord
```sh
@Bot Send a meme! 
@Bot Stop!
```
Send the first one to summon the bot to send a meme.
Send the second if you want the bot server to quit.
### Todos

Add accessibility to private pages by secure login into instagram

License
----

MIT