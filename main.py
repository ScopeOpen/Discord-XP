import discum
import os
import ctypes
from colorama import Fore, Style
import platform
import cv2 
import glob
import re
import random
import json
import reprlib
# CMD PROMPT TOP WINDOW
ctypes.windll.kernel32.SetConsoleTitleW(f"Discord XP [{platform.system()}]")

# EDIT THIS ↓

phrases_Content = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
]

channel_Content = [
    '1',
    '2',
    '3',
    '4',
]













# EDIT THIS ↑

# RANDOM STUFF
sent = 0
os = os.system
b = Style.BRIGHT

# GETTING ACC TOKEN
with open('config.json') as f:
   data = json.load(f)
    
    
# MEME STUFF
pathfiles = 'path/to/files/'
ext = ['png', 'jpg', 'gif', 'mp4']
files = []
[files.extend(glob.glob(pathfiles + '*.' + e)) for e in ext]

# COLOR DEFINITIONS
color1 = b+Fore.GREEN
color2 = b+Fore.WHITE
color3 = b+Fore.GREEN

# VERSION OF APPLICATION
__version__ = 1

# TIMES WHERE MESSAGES WILL BE SENT
SendMessageTime = round(random.uniform(5, 10), 2) # EDIT THIS!

# SHOWING ALL FILES IN /memes/ DIRECTORY
memes = [cv2.imread(file) for file in files]

# RESETING OS DEFINITION
import os

# ALL OUT TXT FILES
phrasesFile = "phrases.txt"
channelsFile = "channels.txt"
memechannelFile = "memechannel.txt"

# GETTING INFO OFF THOSE TXT FILES

# PHRASES TXT FILE READING
if os.path.isfile(phrasesFile):
    OpenPhrases = open(phrasesFile, "r")
    lines1 = OpenPhrases.read()
    PhrasesContents = lines1.splitlines()
    OpenPhrases.close()
 
# ALL CHANNELS TXT FILE READING
if os.path.isfile(channelsFile):
    OpenChannel = open(channelsFile, "r")
    lines2 = OpenChannel.read()
    ChannelContents = lines2.splitlines()
    OpenChannel.close()

# MEME CHANNEL TXT FILE READING
if os.path.isfile(memechannelFile):
    OpenMeme = open(memechannelFile, "r")
    lines3 = OpenMeme.read()
    MemeContents = lines3.splitlines()
    OpenMeme.close()


# USER TOKEN
UserToken = data["userinfo"]["token"]
print(UserToken)

# ALL CONTENTS OF TXT FILES
phrases = PhrasesContents
memeChannel = MemeContents
channels = ChannelContents

# RANDOM CHOICE


fixed1 = ", ".join( repr(e) for e in phrases)
fixed2 = [fixed1]
fixed3 = random.choice(fixed2)
print(fixed3)



# JUST TESTING IF READING FILES WORKS
print(phrases)
print(memeChannel)
print(channels)


# split

FirstText = f"""
        
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗      ██╗  ██╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗     ╚██╗██╔╝██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║█████╗╚███╔╝ ██████╔╝
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║╚════╝██╔██╗ ██╔═══╝ 
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ██╔╝ ██╗██║     
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚════╝       ╚═╝  ╚═╝╚═╝ {color3}v{__version__}
                                                                                  
{Fore.WHITE}                           Made By Scope

{Fore.RESET}"""

Step1 = FirstText.replace("╝", f"{color1}╝")
Step2 = Step1.replace("═", f"{color1}═")
Step3 = Step2.replace("╚", f"{color1}╚")
Step4 = Step3.replace("╗", f"{color1}╗")
Step5 = Step4.replace("║", f"{color1}║")
Step6 = Step5.replace("╔", f"{color1}╔")
LastOutput = Step6.replace("█", f"{color2}█")

print(LastOutput)


# SPLIT



    
test = "3"
test5 = "450"
test2 = [phrases]

    
bot = discum.Client(token=UserToken)

while True:
   bot.sendMessage(random.choice(channel_Content),random.choice(phrases_Content))
    


 




