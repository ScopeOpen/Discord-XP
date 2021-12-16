import discum
import os
import ctypes
from colorama import Fore, Style
import platform
import cv2 
import glob
import re
import random

# CMD PROMPT TOP WINDOW
ctypes.windll.kernel32.SetConsoleTitleW(f"Discord XP [{platform.system()}]")

# RANDOM STUFF
sent = 0
os = os.system
b = Style.BRIGHT

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
xptime = ['TIME1', 'TIME2']

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


# ALL CONTENTS OF TXT FILES
phrases = PhrasesContents
memeChannel = MemeContents
phrases = PhrasesContents

# JUST TESTING IF READING FILES WORKS
print(PhrasesContents)
print(ChannelContents)
print(MemeContents)


def main():

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
    



if __name__ == '__main__':
    main()


 
