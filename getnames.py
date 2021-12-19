import os
from colorama import Fore, Style
b = Style.BRIGHT

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        


my_file = open("images.txt", "w")

dirName = 'memes/';
listOfFiles = getListOfFiles(dirName)
for elem in listOfFiles:
    my_file.writelines(elem + '\n')




        
