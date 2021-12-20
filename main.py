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
b = Style.BRIGHT
ctypes.windll.kernel32.SetConsoleTitleW(f"Discord XP [{platform.system()}]")

w = b+Fore.WHITE

with open('theme.json') as f:
    t__ = json.load(f)
theme = t__.get('theme')
if theme == "blue":
    c = Fore.CYAN
elif theme == "red":
    c = Fore.RED
elif theme == "purple":
    c = Fore.MAGENTA
elif theme == "green":
    c = Fore.GREEN
elif theme == "gray":
    c = Fore.BLACK
else:
    os.system("cls")
    print(f"{w}Invalid {b+Fore.RED}theme.json{w}: {b+Fore.RED}{theme}\n{w}Please change to one of these:\n{b+Fore.CYAN}blue\n{b+Fore.RED}red\n{b+Fore.MAGENTA}purple\n{b+Fore.GREEN}green\n{b+Fore.BLACK}gray{Fore.RESET}")
    e=input(f"press enter...")
    os._exit(os.X_OK)



phrases_Content = []

channel_Content = []

images_Content = []



os = os.system


# GETTING ACC TOKEN
with open('config.json') as f:
   data = json.load(f)
    
    
# MEME STUFF
pathfiles = '/memes/'
ext = ['png', 'jpg', 'gif', 'mp4']
files = []
[files.extend(glob.glob(pathfiles + '*.' + e)) for e in ext]

# COLOR DEFINITIONS


# VERSION OF APPLICATION
__version__ = 1

memes = [cv2.imread(file) for file in files]
print(memes)
import os

phrasesFile = "phrases.txt"
channelsFile = "channels.txt"
memechannelFile = "memechannel.txt"
UserToken = data["userinfo"]["token"]

def cls():
    os.system("cls")
cls()


if theme == "blue":
        color1 = b+Fore.CYAN
        color2 = b+Fore.WHITE
        color3 = b+Fore.BLUE
elif theme == "red":
        color1 = b+Fore.RED
        color2 = b+Fore.WHITE
        color3 = Fore.LIGHTRED_EX
elif theme == "purple":
        color1 = b+Fore.MAGENTA
        color2 = b+Fore.WHITE
        color3 = Fore.LIGHTMAGENTA_EX
elif theme == "green":
        color1 = b+Fore.GREEN
        color2 = b+Fore.WHITE
        color3 = Fore.LIGHTGREEN_EX
elif theme == "gray":
        color1 = b+Fore.BLACK
        color2 = b+Fore.WHITE    
        color3 = b+Fore.LIGHTBLACK_EX

def AppendChannels():
    with open('channels.txt') as file:
        while (line := file.readline().rstrip()):
            channel_Content.append(line)
    print(f"{w}{w}{color3}[{w}Discord-XP{color3}]{w}:{color3}[{w}UpdateChannels{color3}] Completed! Everything is up to date. ") 

def ReturnHome():
    
    FFirstText = f"""
{color1}┌─────────{color1}───────────────────────────{color3}────────────────────────────────────┐
{color1}[{w}1{color1}]  {w}Return Home                                            Exit  {color3}[{w}2{color3}]
{color1}└─────────{color1}───────────────────────────{color3}────────────────────────────────────┘
    """
    print(FFirstText)
    option_choic2e=input(f"{w}{color3}[{w}Discord-XP{color3}] Choice{w}: ")
    if option_choic2e == "1":
        cls()
        Menu()
        Settings()
    if option_choic2e == "2":
        cls()
        exit()

def RunMessage():
    TTTime = 0
    TWordsSent = 0
    TImagesSent = 0
    WordsSent = 0
    ImagesSent = 0
    bot = discum.Client(token=UserToken)

    MessageFirst = data["messages"]["firstTime"]
    MessageSecond = data["messages"]["secondTime"]
    ImagesFirst = data["images"]["firstTime"]
    ImagesSecond = data["images"]["secondTime"]
    while True:
        TTTime = round(random.uniform(5, 10), 3)
        pause.seconds(TTTime)
        bot.sendFile(data["serverinfo"]["memes"],'memes/'+random.choice(images_Content),False)
        cls()
        ImagesSent += 1
        TWordsSent += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Sending Images... Images Sent [{ImagesSent}], Words Sent [{TWordsSent}] [May Be Inacurate Due To Ratelimiting.] -- [Pause Time [{TTTime}]]")
        print(f'{w}{color3}[{w}Discord-XP{color3}] Sent IMAGES{w}: {color3}[{w}{ImagesSent}{color3}]')

        while True:
            TTTime = round(random.uniform(5, 10), 3)
            pause.seconds(TTTime)

            bot.sendMessage(random.choice(channel_Content),random.choice(phrases_Content))
            cls()
            WordsSent += 1
            TWordsSent += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Sending Messages... Images Sent [{ImagesSent}], Words Sent [{TWordsSent}] [May Be Inacurate Due To Ratelimiting.] -- [Pause Time [{TTTime}]]")
            print(f'{w}{color3}[{w}Discord-XP{color3}] Sent WORDS{w}: {color3}[{w}{TWordsSent}{color3}]')
            if WordsSent == random.randint(MessageFirst, MessageSecond):
                WordsSent=0
                break

    



def getPhrases():
    with open('txt/phrases.txt') as file:
        while (line := file.readline().rstrip()):
            phrases_Content.append(line)
    print(f"{w}{w}{color3}[{w}Discord-XP{color3}]{w}:{color3}[{w}UpdatePhrases{color3}] Completed! Everything is up to date. ") 


def getFiles(): 
    for filename in os.listdir("./memes"):
        images_Content.append(filename)
    print(f"{w}{w}{color3}[{w}Discord-XP{color3}]{w}:{color3}[{w}UpdateImages{color3}] Completed! Everything is up to date.") 

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
def centerize(l:list,w:int)->str:
    padding =  ' '*(w//2)
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)


def Menu():
    print(data)
    FirstText = f"""
        
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗      ██╗  ██╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗     ╚██╗██╔╝██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║█████╗╚███╔╝ ██████╔╝
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║╚════╝██╔██╗ ██╔═══╝ 
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ██╔╝ ██╗██║     
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚════╝       ╚═╝  ╚═╝╚═╝ {color3}v{__version__}                                                                               
    {Fore.RESET}"""
    Step1 = FirstText.replace("╝", f"{color1}╝")
    Step2 = Step1.replace("═", f"{color1}═")
    Step3 = Step2.replace("╚", f"{color1}╚")
    Step4 = Step3.replace("╗", f"{color1}╗")
    Step5 = Step4.replace("║", f"{color1}║")
    Step6 = Step5.replace("╔", f"{color1}╔")
    LastOutput = Step6.replace("█", f"{color2}█")
    print(LastOutput)

def Settings():
    FFirstText = f"""
{color1}┌─────────{color1}───────────────────────────{color3}────────────────────────────────────┐
{color1}[{w}1{color1}]  {w}Update Images                                            Run Bot  {color3}[{w}4{color3}]
{color1}[{w}2{color1}]  {w}Update Phrases                                                      {color3}]
{color1}[{w}3{color1}]  {w}Update Channels                                             Exit  {color3}[{w}5{color3}]
{color1}└─────────{color1}───────────────────────────{color3}────────────────────────────────────┘
    """
    print(FFirstText)
    option_choice=input(f"{w}{color3}[{w}Discord-XP{color3}] Choice{w}: ")

    if option_choice == "1":
        getFiles()
        pause.seconds(1)
        cls()
        Menu()
        Settings()
    elif option_choice == "2":
        getPhrases()
        pause.seconds(1)
        cls()
        Menu()
        Settings()
    elif option_choice == "3":
        AppendChannels()
        pause.seconds(1)
        cls()
        Menu()
        Settings()
        print(channel_Content)
    elif option_choice == "4":
        cls()
        RunMessage()
    elif option_choice == "5":
        cls()
        exit()
    
    else:
        print(f'{w}{color3}[{w}Discord-XP{color3}] Invalid.')
        pause.seconds(1)
        cls()
        Menu()
        Settings()


Menu()
Settings()
