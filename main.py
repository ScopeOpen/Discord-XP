import discum
import os
import ctypes
from colorama import Fore, Style
import platform
import cv2 
import glob
import re

ctypes.windll.kernel32.SetConsoleTitleW(f"Discord XP [{platform.system()}]")

sent = 0
os = os.system
b = Style.BRIGHT

pathfiles = 'path/to/files/'
ext = ['png', 'jpg', 'gif', 'mp4']
files = []
[files.extend(glob.glob(pathfiles + '*.' + e)) for e in ext]

color1 = b+Fore.GREEN
color2 = b+Fore.WHITE

__version__ = 1



phrases = [
  
]

channels = [

]

memechannelS = [

]

xptime = ['TIME1', 'TIME2']


memes = [cv2.imread(file) for file in files]

def main():

    FirstText = f"""
        
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗      ██╗  ██╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗     ╚██╗██╔╝██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║█████╗╚███╔╝ ██████╔╝
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║╚════╝██╔██╗ ██╔═══╝ 
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ██╔╝ ██╗██║     
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚════╝       ╚═╝  ╚═╝╚═╝     
                                                                                  


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

