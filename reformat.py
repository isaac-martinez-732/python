from asyncio.windows_events import NULL
import sys
import os  
import re
from os.path import isfile, join, isdir
import fitz

# Arguments passed
def isSquadronSignal (root):
    return root == "Squadron Signal" or root == "Concord"

def preffixForSquadronSignal (folder):
    if folder == "Aircraft in Action" : preffix = "1"
    elif folder == "Mini in Action" : preffix = "16"
    elif folder == "Armor in Action" : preffix = "2"
    elif folder == "Combat Troops in Action" : preffix = "3"
    elif folder == "Warships in Action" : preffix = "4"
    elif folder == "Modern Military Aircraft" : preffix = "5"
    elif folder == "Aircraft Walk Around" : preffix = "55"
    elif folder == "Armor Walk Around" : preffix = "57"
    elif folder == "Fighting Colors" : preffix = "65"
    elif folder == "In Detail & Scale" : preffix = "82"
    elif folder == "General" : preffix = "6"
    elif folder == "Groups & Squadrons" : preffix = "61"
    elif folder == "Armor at War" : preffix = "7"
    elif folder == "Colors & Markings" : preffix = "84"
    else: preffix = "0"

    return preffix


def basicFormat(newFileName, root):
    newFileName = newFileName.replace(root, "")
    newFileName = newFileName.replace(root.lower(), "")
    newFileName = newFileName.replace(root.upper(), "")
    newFileName = newFileName.replace(token, "")
    newFileName = newFileName.replace("nº", "")
    newFileName = newFileName.replace(token.lower(), "")
    newFileName = newFileName.replace(token.upper(), "")
    newFileName = correctFilename +  newFileName
    print(newFileName)
    return newFileName

def clean (filename):
    newFileName = filename
    ##print("entro al clean")
    newFileName = newFileName.replace(" PDF ", "")
    newFileName = newFileName.replace(" Pdf ", "")
    newFileName = newFileName.replace("[Aviation]", "")
    newFileName = newFileName.replace("[aviation]", "")
    newFileName = newFileName.replace("- Aircraft-", "-")  
    newFileName = newFileName.replace("nº N ", "nº")
    newFileName = newFileName.replace("nº(N ", "nº")
    newFileName = newFileName.replace("ºº", "º")
    newFileName = newFileName.replace("nÂº", "nº")
    newFileName = newFileName.replace("Nâ", "nº")
    
    newFileName = newFileName.replace("nºnº", "nº")
    newFileName = newFileName.replace("nºn°", "nº")
    newFileName = newFileName.replace("nºn", "nº")
    newFileName = newFileName.replace("Nº", "nº")
    newFileName = newFileName.replace("n_", "nº")
    newFileName = newFileName.replace("No.", "nº")
    newFileName = newFileName.replace("- -", "-")
    newFileName = newFileName.replace("-  -", "-")
    newFileName = newFileName.replace("  ", " ")
    newFileName = newFileName.replace("--", "-")
    newFileName = newFileName.replace("_", "-")
    newFileName = newFileName.replace("[]", "")
    newFileName = newFileName.replace("]", ")")
    newFileName = newFileName.replace("[", "(")
    
    newFileName = newFileName.replace("()", "")
    newFileName = newFileName.replace("( ", "(")
    newFileName = newFileName.replace("((", "(")
    newFileName = newFileName.replace("))", ")")
    newFileName = newFileName.replace("Ebook", "")
    newFileName = newFileName.replace("ebook", "")
    newFileName = newFileName.replace("Â", "")
    newFileName = newFileName.replace("Ã", "")
    newFileName = newFileName.replace("°", "")   
    newFileName = newFileName.replace("delPrado", "")
    newFileName = newFileName.replace("DelPrado", "")
    newFileName = newFileName.replace("Delprado", "")
    newFileName = newFileName.replace("Militaria", "")
    newFileName = newFileName.replace("Publishing", "")
    newFileName = newFileName.replace("Series", "")
    newFileName = newFileName.replace("Men-At-Arms", "")
    newFileName = newFileName.replace("Men-at-Arms", "")
    newFileName = newFileName.replace("Men At Arms", "")
    newFileName = newFileName.replace("Men at arms", "")
    newFileName = newFileName.replace("Men.at.Arms", "")
    newFileName = newFileName.replace("Aircraft of Aces", "")
    newFileName = newFileName.replace("Aircraft Of The Aces", "")
    newFileName = newFileName.replace("Squadron-Signal", "")
    newFileName = newFileName.replace("In Action", "")
    newFileName = newFileName.replace("in action", "")  

    
    newFileName = newFileName.replace("(Armor nº","(Armor in Action nº")
    newFileName = newFileName.replace("(Combat Troops nº","(Combat Troops in Action nº")
    newFileName = newFileName.replace("Books", "")

    
    #newFileName = newFileName[0:-4].replace(".", " ") + newFileName[-4:]
    return newFileName

def seekEpubConverts(token):
    
    if token == "Aircraft of the Aces" : 
        if int(newFileName[len(correctFilename):len(correctFilename)+intSize]) == 31 : 
            maxsize  = 145
        else: 
            maxsize  = 137
    elif token == "Aviation Elite" : maxsize  = 132
    elif token == "Air Campaign" : maxsize  = 98
    elif token == "Air Vanguard" : maxsize  = 68
    elif token == "Battle Orders" : maxsize  = 100
    elif token == "Campaign" :
        if int(newFileName[len(correctFilename):len(correctFilename)+intSize]) == 52 : 
            maxsize  = 132
        else: 
            maxsize  = 111
    elif token == "Combat" : maxsize  = 87
    elif token == "Combat Aircraft" : maxsize  = 115
    elif token == "Command" : maxsize  = 97
    elif token == "Dogfight" : maxsize  = 97
    elif token == "Duel" : maxsize  = 97
    elif token == "Elite" : maxsize  = 103
    elif token == "Essential Histories" : maxsize  = 148
    elif token == "Essential Histories Specials" : maxsize  = 351
    elif token == "Field Of Glory" : maxsize  = 175 
    elif token == "Fortress" : maxsize  = 70    
    elif token == "Frontline Colour" : maxsize  = 131   
    elif token == "Graphic History" : maxsize  = 97
    elif token == "Men at Arms" : maxsize  = 68
    elif token == "Modelling" : maxsize  = 150
    elif token == "New Vanguard" : maxsize  = 97
    elif token == "Order of Battle" : maxsize  = 104
    elif token == "Production Line to Frontline" : maxsize  = 147
    elif token == "Raid" : maxsize  = 97
    elif token == "Superbase" : maxsize  = 130
    elif token == "Warrior" : maxsize  = 97
    elif token == "Wargames" : maxsize  = 109
    elif token == "Weapon" : maxsize  = 97
    elif token == "X-Planes" : maxsize  = 97
    else:
       maxsize  = 100
    try:
        if newFileName[-4:] == ".pdf":
            doc = fitz.open(subdir + "\\" + newFileName) 
            if maxsize < len(doc): print(  newFileName + "-"  + str(len(doc)))
            if len(doc) == 0 : print(  newFileName + "-"  + str(len(doc)))
            if len(doc) < (maxsize/4) :  print(  newFileName + "-"  + str(len(doc)))
    except:
        print("couldn't read " + newFileName)

def findMissing (token,test_list):
    if token == "Aircraft of the Aces" : maxE  = 137
    elif token == "Aviation Elite" : maxE  = 41
    elif token == "Air Campaign" : maxE  = 33
    elif token == "Air Vanguard" : maxE  = 23
    elif token == "Battle Orders" : maxE  = 38
    elif token == "Campaign" : maxE  = 383
    elif token == "Combat" : maxE  = 67
    elif token == "Combat Aircraft" : maxE  = 146
    elif token == "Command" : maxE  = 32
    elif token == "Dogfight" : maxE  = 5
    elif token == "Duel" : maxE  = 124
    elif token == "Elite" : maxE  = 247
    elif token == "Essential Histories" : maxE  = 78
    elif token == "Essential Histories Specials" : maxE  = 7
    elif token == "Fortress" : maxE  = 113    
    elif token == "Graphic History" : maxE  = 12
    elif token == "Men at Arms" : maxE  = 548
    elif token == "New Vanguard" : maxE  = 314
    elif token == "Raid" : maxE  = 58
    elif token == "Warrior" : maxE  = 183
    elif token == "Weapon" : maxE  = 84
    elif token == "X-Planes" : maxE  = 17
    else:
       maxE  = max(test_list)
    res = [ele for ele in range(maxE+1) if ele not in test_list]
    res.pop(0)
    # print result
    if len(res) > 0 : print("Missing on " +token+": " + str(res) )
    return len(res)

def findDupes (token,test_list):
 
   dupes = [x for n, x in enumerate(test_list) if x in test_list[:n]]
   if len(dupes) >0 : print("Dupes on " +token+": " + str(dupes))
   return len(dupes)

#START SCRIPT
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
for l in range(len(publishers)):
    if len(publishers) == 1 : publisherDir = path   
    else :  publisherDir = path   + "\\" + publishers[l]
    print("---------------Publisher: " +  str(publishers[l]))
    onlyDirs = [f for f in os.listdir(publisherDir ) if isdir(join(publisherDir, f))]
    totalPub = 0
    missingPub = 0

    for k in range(len(onlyDirs)):
        token = onlyDirs[k]
        subdir = publisherDir + "\\" + token
        onlyfiles = [f for f in os.listdir(subdir) if isfile(join(subdir, f))]
        correctFilename = publishers[l]    + " ("+ token + " nº"
        fullList = []
        for i in range(len(onlyfiles)):
            fixed = False
            newFileName = onlyfiles[i]
            j= 0
            if newFileName[-4:] == '.xls': continue
            regexOnly2digits = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][^\d]")
            regexOnly1digit = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][^\d]")
            regex3digitsnoPar = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9][^\)]")
            regex4digitsnoPar = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9][0-9][^\)]")
            regex3digitsPar = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9]\)[^\s][^-][^\s]")
            regex4digitsPar = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9][0-9]\)[^\s][^-][^\s]")
            regex3digitsParSpace = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9]\)\s[^-]")
            regex4digitsParSpace = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9][0-9]\)\s[^-]")
            regex3digitsNoLastSpace = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9]\)\s[-][^\s]")
            regex4digitsNoLastSpace = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9][0-9]\)\s[-][^\s]")
            regexfinal = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9]\) - ")
            regexfinalSS = re.compile("^"+ publishers[l] +" \(" + token +" nº[0-9][0-9][0-9][0-9]\) - ")
            
            while not fixed:
                newFileName = clean(newFileName)
                #print(newFileName)
                if j>0 : print(j) 
                if newFileName.startswith(correctFilename + " "):
                    newFileName = newFileName.replace(correctFilename +" ", correctFilename)
                elif newFileName.startswith(correctFilename + "-"):
                    newFileName = newFileName.replace(correctFilename +"-", correctFilename)
                elif newFileName.startswith(correctFilename + "nº"):
                    newFileName = newFileName.replace(correctFilename +"nº", correctFilename)
                elif newFileName.startswith(correctFilename + ","):
                    newFileName = newFileName.replace(correctFilename +",", correctFilename)
                elif newFileName.startswith(correctFilename + "("):
                    newFileName = newFileName.replace(correctFilename +"(", correctFilename)
                elif newFileName.startswith(correctFilename + ")"):
                    newFileName = newFileName.replace(correctFilename +")", correctFilename)
                elif newFileName.startswith(correctFilename + "["):
                    newFileName = newFileName.replace(correctFilename +"[", correctFilename)
                elif newFileName.startswith(correctFilename + "]"):
                    newFileName = newFileName.replace(correctFilename +"]", correctFilename)
                elif newFileName.startswith(correctFilename + "#"):
                    newFileName = newFileName.replace(correctFilename +"#", correctFilename)
                elif newFileName.startswith(correctFilename + "."):
                    newFileName = newFileName.replace(correctFilename +".", correctFilename)
                elif regexOnly2digits.search(newFileName):
                    if isSquadronSignal(publishers[l]):
                        if len(preffixForSquadronSignal(token)) > 1 :
                            newFileName = newFileName.replace(correctFilename, correctFilename+ preffixForSquadronSignal(token))
                        else:
                            newFileName = newFileName.replace(correctFilename, correctFilename+ preffixForSquadronSignal(token) + "0")
                    else:
                        newFileName = newFileName.replace(correctFilename, correctFilename+ "0")
                elif regexOnly1digit.search(newFileName):
                    newFileName = newFileName.replace(correctFilename, correctFilename+ "00")
                elif regex3digitsnoPar.search(newFileName):
                    if isSquadronSignal(publishers[l]):
                        if len(preffixForSquadronSignal(token)) > 1 : newFileName = newFileName.replace(correctFilename +"0", correctFilename)
                        if regex4digitsnoPar.search(newFileName):
                            newFileName = newFileName[0:len(correctFilename)+intSizeSS] + ") - " + newFileName[len(correctFilename)+intSizeSS:]
                        elif regex4digitsPar.search(newFileName):
                            newFileName = newFileName[0:len(correctFilename)+intSizeSS +1] + " - " + newFileName[len(correctFilename)+intSizeSS +1:]
                        elif regex4digitsParSpace.search(newFileName):
                            newFileName = newFileName[0:len(correctFilename)+intSizeSS +2] + "- " + newFileName[len(correctFilename)+intSizeSS +2:]
                        elif regex4digitsNoLastSpace.search(newFileName):
                            newFileName = newFileName[0:len(correctFilename)+intSizeSS +3] + " " + newFileName[len(correctFilename)+intSizeSS +3:]
                        elif regexfinalSS.search(newFileName):
                            fixed = True 
                            if len(preffixForSquadronSignal(token)) > 1 : fullList.append(int(newFileName[len(correctFilename)+2:len(correctFilename)+intSizeSS]))
                            else: fullList.append(int(newFileName[len(correctFilename)+1:len(correctFilename)+intSizeSS]))
                        elif regex3digitsnoPar.search(newFileName):
                            newFileName = newFileName.replace(correctFilename, correctFilename+ preffixForSquadronSignal(token))
                    else:
                        newFileName = newFileName[0:len(correctFilename)+intSize] + ") - " + newFileName[len(correctFilename)+intSize:]
                elif regex3digitsPar.search(newFileName):
                    if len(preffixForSquadronSignal(token)) > 1 : newFileName = newFileName.replace(correctFilename +"0", correctFilename)
                    newFileName = newFileName[0:len(correctFilename)+intSize +1] + " - " + newFileName[len(correctFilename)+intSize +1:]
                elif regex3digitsParSpace.search(newFileName):
                    if len(preffixForSquadronSignal(token)) > 1 : newFileName = newFileName.replace(correctFilename +"0", correctFilename)
                    newFileName = newFileName[0:len(correctFilename)+intSize +2] + "- " + newFileName[len(correctFilename)+intSize +2:]
                elif regex3digitsNoLastSpace.search(newFileName):
                    if len(preffixForSquadronSignal(token)) > 1 : newFileName = newFileName.replace(correctFilename +"0", correctFilename)
                    newFileName = newFileName[0:len(correctFilename)+intSize +3] + " " + newFileName[len(correctFilename)+intSize +3:]
                elif regexfinal.search(newFileName):
                    if isSquadronSignal(publishers[l]):
                        newFileName = newFileName.replace(correctFilename, correctFilename+ preffixForSquadronSignal(token))
                    else:
                        newFileName = clean(newFileName)
                        ##print("nothing to do here")
                        fullList.append(int(newFileName[len(correctFilename):len(correctFilename)+intSize]))
                    fixed = True
                elif regexfinalSS.search(newFileName): 
                    if isSquadronSignal(publishers[l]): 
                        fixed = True
                        if token == "Aircraft Walk Around" : fullList.append(int(newFileName[len(correctFilename)+2:len(correctFilename)+intSizeSS]))
                        else: fullList.append(int(newFileName[len(correctFilename)+1:len(correctFilename)+intSizeSS]))
                    else:
                        newFileName = newFileName[0:len(correctFilename)] + newFileName[len(correctFilename)+1:]
                else:
                    print("entro en el else")
                    newFileName = basicFormat(newFileName,publishers[l] )
                    
                j+=1
                if j> 10 : break
                newFileName = clean(newFileName)
            if onlyfiles[i] != newFileName:
                try:
                    os.rename(subdir + "\\" + onlyfiles[i],subdir + "\\" + newFileName)
                except FileExistsError:
                    ext = newFileName[-4]
                    newFileName = newFileName.replace(ext, "(1)" + ext)
                    os.rename(subdir + "\\" + onlyfiles[i],subdir + "\\" + newFileName)

            seekEpubConverts(token)
            
            
        missingPub += findMissing(token, fullList)
        totalPub -= findDupes(token,fullList)  
        totalPub += len(fullList)
        fullList =[]
    if totalPub + missingPub >0 :
        formatted_float = "{:.3f}".format( 100* (totalPub/(missingPub+totalPub)))
        print("---------------Total: " + str(totalPub) + " Missing: " + str(missingPub) + " Complete: " + str(formatted_float) + "%")
    print("")
    total += totalPub
    missing += missingPub
formatted_float = "{:.3f}".format(100* (total/(missing+total)))    
print("TOTAL ALL: " + str(total) + " MISSING ALL: " + str(missing) + " COMPLETE ALL: " + str(formatted_float) + "%")
input("Press Enter to continue...")
