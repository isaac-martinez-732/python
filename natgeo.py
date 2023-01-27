
from asyncio.windows_events import NULL
from fileinput import filename
import sys
import os  
import re
import calendar
import fitz

from os.path import isfile, join, isdir

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def putDate(newFileName, magazine):
    text = newFileName[len(correctFilename)+intSize+len(") - "):-4]
    number = newFileName[len(correctFilename):len(correctFilename)+intSize]
    month = 0
    year =0
    for j in range(len(months)):
        if newFileName.lower().find(months[j]) > -1:
            month = j
    for y in range(2023-1998 +1 ) :
        if newFileName.find(str(1998+y)) > -1: 
            year = 1998+y
    correctnumber = (((year - 1998) - 1) * 12) + 3 + month + 1   #"octubre 1997 = 1"
    if number.isdigit(): 
        if correctnumber != int(number) : print (newFileName + "--> " + str(correctnumber))
    else :
        print (newFileName + "--> " + str(correctnumber))
    return correctnumber

        

    

##START SCRIPT
initialYear = 1976
finalYear  = 2023
yearsRange = finalYear - initialYear +1
months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
if  len(sys.argv) > 1:
    path = os.getcwd() + "\\" + sys.argv[1]
    publishers = [sys.argv[1]]
else: 
    path = os.getcwd() + "\\"
    publishers = [f for f in os.listdir(path) if isdir(join(path, f))]
total = 0
missing = 0  
intSizeSS = 4
intSize = 3
missingMag = []
fullMag = []
years = [0] * (yearsRange)
fulldate = [[0]*12 for i in range(yearsRange)]

for l in range(len(publishers)):
    if len(publishers) == 1 : publisherDir = path   
    else :  publisherDir = path   + "\\" + publishers[l]
    print("---------------Publisher: " +  str(publishers[l]))
    onlyDirs = [f for f in os.listdir(publisherDir ) if isdir(join(publisherDir, f))]
    
    for k in range(len(onlyDirs)):
        magazine = onlyDirs[k]
        subdir = publisherDir + "\\" + magazine
        onlyfiles = [f for f in os.listdir(subdir) if isfile(join(subdir, f))]
        correctFilename = publishers[l]    + " ("+ magazine + " nº"
        fullList = []
        if magazine == "National Geographic" :
            for i in range(len(onlyfiles)):
                putDate(onlyfiles[i], magazine)

            
        
    print("")
input("Press Enter to continue...")

