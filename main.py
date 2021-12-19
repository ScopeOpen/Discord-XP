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
import pause
# CMD PROMPT TOP WINDOW
TWordsSent = 0
TImagesSent = 0
WordsSent = 0
ImagesSent = 0
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
    '',
]




from skimage.io import imread_collection

#your path 
col_dir = 'memes/*.png'

#creating a collection with the available images
col = imread_collection(col_dir)

lst_str = str(col)[1:-1] 
lst_strr = [lst_str]

print(lst_strr)
print(col)




# EDIT THIS ↑

# RANDOM STUFF

os = os.system
b = Style.BRIGHT

# GETTING ACC TOKEN
with open('config.json') as f:
   data = json.load(f)
    
    
# MEME STUFF
pathfiles = '/memes/'
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


# SHOWING ALL FILES IN /memes/ DIRECTORY
memes = [cv2.imread(file) for file in files]
print(memes)
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


bot = discum.Client(token=UserToken)


TTTime = 0

while True:
    TTTime = round(random.uniform(5, 10), 3)
    pause.seconds(TTTime)

    bot.sendFile(data["serverinfo"]["memes"],'memes\lol.png',False)
    ImagesSent += 1
    TImagesSent += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Sending Images... Images Sent [{TImagesSent}], Words Sent [{TWordsSent}] [May Be Inacurate Due To Ratelimiting.] -- [Pause Time [{TTTime}]]")

    while True:
        TTTime = round(random.uniform(5, 10), 3)
        pause.seconds(TTTime)

        bot.sendMessage(random.choice(channel_Content),random.choice(phrases_Content))
        WordsSent += 1
        TWordsSent += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Sending Images... Images Sent [{TImagesSent}], Words Sent [{TWordsSent}] [May Be Inacurate Due To Ratelimiting.] -- [Pause Time [{TTTime}]]")
        if WordsSent == round(random.uniform(5, 10), 1):
            break
        
  





