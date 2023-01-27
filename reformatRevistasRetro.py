
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
    number = int(newFileName[len(correctFilename):len(correctFilename)+intSize])
    
    if text != "": 
        filenameWithDate  = newFileName
        month = text.split()[0]
        if len(text.split()) >1:
            year = text.split()[1]
    else :
        filenameWithDate  = newFileName   
    

    return filenameWithDate


def extractCover(publisher , ruta, fileName):
    root = "F:\\Portadas\\"
    newFilename = fileName[0:-4].replace("pdf", "")
    cover = root  + publisher + "\\"+ ruta + "\\" + newFilename +".png"
    if not(os.path.isdir(root + publisher)): os.mkdir(root + publisher)
    if not(os.path.isdir(root + publisher+ "\\" +ruta )): os.mkdir(root + publisher+ "\\" +ruta)
    if (not os.path.exists(cover)) :
        try:
            pdf_document = fitz.open( os.getcwd() + "\\" +publisher + "\\"+ ruta + "\\" + fileName)
            i = 0
            for image in pdf_document.get_page_images(0):
                xref = image[0]
                pix = fitz.Pixmap(pdf_document, xref)
                #image_base = pdf_document.extractImage(xref)
                ##bytes_image = image_base["image"]
                ##print(str(bytes_image) + " bytes?")
                if pix.n < 5:        # this is GRAY or RGB
                    try:
                        pix.save(cover)
                        print(cover + " created")
                    except ValueError:
                        NULL
                        #print (str(pix.n))
                        #print(cover + " not created")
                else:                # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.save(cover)
                    print(cover + " created")
                    pix1 = None
                pix = None
                i += 1
                if i > 0 : break
        except fitz.fitz.FileDataError:
            print (ruta + "\\" + fileName)

def basicFormat(newFileName, root):
    newFileName = newFileName.replace(root, "")
    newFileName = newFileName.lower().replace(root.lower(), root)
    newFileName = newFileName.lower().replace(magazine.lower(), magazine)
    newFileName = newFileName.replace(root.lower(), "")
    newFileName = newFileName.replace(root.upper(), "")
    newFileName = newFileName.replace(magazine, "")
    newFileName = newFileName.replace("nº", "")
    newFileName = newFileName.replace(magazine.lower(), "")
    newFileName = newFileName.replace(magazine.upper(), "")

    newFileName = correctFilename +  newFileName
    print(newFileName)
    return newFileName

def clean (filename):
    newFileName = filename
    ##print("entro al clean")
    newFileName = newFileName.replace("ROD_ES_", "")
    newFileName = newFileName.replace("ROD ES ", "")
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
    newFileName = newFileName.replace("_", " ")
    newFileName = newFileName.replace("[]", "")
    newFileName = newFileName.replace("]", ")")
    newFileName = newFileName.replace("[", "(")
    
    newFileName = newFileName.replace("()", "")
    newFileName = newFileName.replace("( ", "(")
    newFileName = newFileName.replace("((", "(")
    newFileName = newFileName.replace("))", ")")
    newFileName = newFileName.replace("Ebook", "")
    newFileName = newFileName.replace("ebook", "")
    newFileName = newFileName.replace("revista", "")
    newFileName = newFileName.replace("Â", "")
    newFileName = newFileName.replace("Ã", "")
    newFileName = newFileName.replace("°", "")   
    newFileName = newFileName.replace("ºã-º", "º")
    newFileName = newFileName[0:-4].replace("PDF", "") + newFileName[-4:]
    newFileName = newFileName.replace("Hobby-Consolas", "")  
    newFileName = newFileName.replace("Superjuegos", "") 
    newFileName = newFileName.replace("micromania", "")
    newFileName = newFileName.replace("ºMicromania", "")
    newFileName = newFileName.replace("Micromanía", "Micromania")
    newFileName = newFileName.replace("superjuegos", "Super Juegos")
     
    newFileName = newFileName.replace("Todosega", "")
   
    newFileName = newFileName.replace("enero", "Enero")
    newFileName = newFileName.replace("febrero", "Febrero")
    newFileName = newFileName.replace("marzo", "Marzo")
    newFileName = newFileName.replace("abril", "Abril")
    newFileName = newFileName.replace("mayo", "Mayo")
    newFileName = newFileName.replace("junio", "Junio")
    newFileName = newFileName.replace("julio", "Julio")
    newFileName = newFileName.replace("agosto", "Agosto")
    newFileName = newFileName.replace("septiembre", "Septiembre")
    newFileName = newFileName.replace("octubre", "Octubre")
    newFileName = newFileName.replace("noviembre", "Noviembre")
    newFileName = newFileName.replace("diciembre", "Diciembre")
    
  
    
    newFileName = newFileName[0:-4].replace(".", " ") + newFileName[-4:]
    return newFileName

def findMissing (magazine,test_list):
    maxE = 0
    minE = 0
    res = 0
    if len(test_list) > 0 : 
        if magazine == "Micromania Tercera Epoca" : maxE  = 326
        elif magazine == "Computer Gaming World" :  maxE  = 71
        elif magazine == "Retro Gamer" :  maxE  = 41
        elif magazine == "Super Juegos" :  maxE  = 193
        elif magazine == "PlanetStation" :  maxE  = 64
        elif magazine == "OK Super Consolas" :  
            minE = 5 
            maxE  = 25
        elif magazine == "MSX Extra" :  
            minE = 11
        elif magazine == "OK PC" :  maxE  = 54
        elif magazine == "Manual" :  maxE  = 12
        elif magazine == "DreamPlanet" :  maxE  = 16
        elif magazine == "Playmania" :  maxE  = 289
        else : maxE  = max(test_list)
        res = [ele for ele in range(minE, maxE+1) if ele not in test_list]
        if  len(res) > 0 :
            res.pop(0)
            if magazine == "MSX Extra" : 
                index = res.index(26)
                res.pop(index)
                index = res.index(8)
                res.pop(index)
                index = res.index(20)
                res.pop(index)
                index = res.index(33)
                res.pop(index)
            elif magazine == "Juegos MSX Extra" : 
                index = res.index(8)
                res.pop(index)
            elif magazine == "MSX Club" : 
                index = res.index(23)
                res.pop(index)
                index = res.index(10)
                res.pop(index)
                index = res.index(17)
                res.pop(index)
                index = res.index(4)
                res.pop(index)
                index = res.index(31)
                res.pop(index)

        # print result
        if len(res) > 0 : print("Missing on " +magazine+": " + str(res) )
        return len(res)
    else : 
        return 0
        

def findDupes (magazine,test_list): 
   dupes = [x for n, x in enumerate(test_list) if x in test_list[:n]]
   if len(dupes) >0 : print("Dupes on " +magazine+": " + str(dupes))
   return len(dupes)

def seekEpubConverts(token,newFileName):
    
    if token == "National Geographic" : maxsize  = 160
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

def findYears (years,fulldate,revista): 
    for y in range(40):
        if revista.find(str(1984+y)) > -1 : 
            years[y] += 1
            for m in range(len(months)):
                if revista.lower().find(str(months[m])) > -1 : 
                    fulldate[y][m] += 1
                       
    return years

def printYears(years):
    totalWithYear = 0
    yearsGrid = "year " + "\t"
    yearsIndex = 0 
    for i in range(len(years)):
        totYears = str(years[i])
        if years[i] < 100 : totYears = " " + totYears
        if years[i] < 10 : totYears = " " + totYears
        if yearsIndex > 9 : 
            yearsIndex = 0 
            print(yearsGrid)
            yearsGrid = "year " + "\t"
            yearsGrid += str(1984+i) + ":" + totYears + "  "  # +"avg " + "{:.1f}".format( years[i]/12) + " " 
        else :
            yearsGrid += str(1984+i) + ":" + totYears + "  "  #+ "avg " + "{:.1f}".format( years[i]/12) + " " 
        totalWithYear +=  years[i]
        yearsIndex += 1
    print(yearsGrid) 
    print(totalWithYear)
    print("{:.3f}".format(100* (totalWithYear/total)))

def printFullDate(fulldate):
    yearsGrid = "year " + "\t"
    totalWithYear = 0
    for i in range(len(fulldate)):
        yearsGrid += str(1984+i)
        for m in range(len(fulldate[i])):
            totMonths = str(fulldate[i][m])
            if fulldate[i][m] < 10 : totMonths = " " + totMonths
            yearsGrid += "  " + months[m] + ":" + totMonths   
            totalWithYear += fulldate[i][m]  
        print(yearsGrid)
        
        yearsGrid = "year " + "\t"
    print(totalWithYear)
    

##START SCRIPT
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
years = [0] * (40)
fulldate = [[0]*12 for i in range(40)]

for l in range(len(publishers)):
    if len(publishers) == 1 : publisherDir = path   
    else :  publisherDir = path   + "\\" + publishers[l]
    print("---------------Publisher: " +  str(publishers[l]))
    onlyDirs = [f for f in os.listdir(publisherDir ) if isdir(join(publisherDir, f))]
    totalPub = 0
    missingPub = 0

    for k in range(len(onlyDirs)):
        magazine = onlyDirs[k]
        subdir = publisherDir + "\\" + magazine
        onlyfiles = [f for f in os.listdir(subdir) if isfile(join(subdir, f))]
        correctFilename = publishers[l]    + " ("+ magazine + " nº"
        fullList = []
        missingRev =  0
        totalRev = 0
        for i in range(len(onlyfiles)):
            fixed = False
            newFileName = onlyfiles[i]
            j= 0
            if newFileName[-4:] != '.pdf': continue
            regexOnly2digits = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][^\d]")
            regexOnly1digit = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][^\d]")
            regex3digitsnoPar = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9][^\)]")
            regex4digitsnoPar = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9][0-9][^\)]")
            regex3digitsPar = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9]\)[^\s][^-][^\s]")
            regex4digitsPar = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9][0-9]\)[^\s][^-][^\s]")
            regex3digitsParSpace = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9]\)\s[^-]")
            regex4digitsParSpace = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9][0-9]\)\s[^-]")
            regex3digitsNoLastSpace = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9]\)\s[-][^\s]")
            regex4digitsNoLastSpace = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9][0-9]\)\s[-][^\s]")
            regexfinal = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9]\) - ")
            regexfinalSS = re.compile("^"+ publishers[l] +" \(" + magazine +" nº[0-9][0-9][0-9][0-9]\) - ")
            
            while not fixed:
                newFileName = clean(newFileName)
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
                    newFileName = newFileName.replace(correctFilename, correctFilename+ "0")
                elif regexOnly1digit.search(newFileName):
                    newFileName = newFileName.replace(correctFilename, correctFilename+ "00")
                elif regex3digitsnoPar.search(newFileName):
                        newFileName = newFileName[0:len(correctFilename)+intSize] + ") - " + newFileName[len(correctFilename)+intSize:]
                elif regex3digitsPar.search(newFileName):
                    newFileName = newFileName[0:len(correctFilename)+intSize +1] + " - " + newFileName[len(correctFilename)+intSize +1:]
                elif regex3digitsParSpace.search(newFileName):
                    newFileName = newFileName[0:len(correctFilename)+intSize +2] + "- " + newFileName[len(correctFilename)+intSize +2:]
                elif regex3digitsNoLastSpace.search(newFileName):
                    newFileName = newFileName[0:len(correctFilename)+intSize +3] + " " + newFileName[len(correctFilename)+intSize +3:]
                elif regexfinal.search(newFileName):
                    newFileName = clean(newFileName)
                    fullList.append(int(newFileName[len(correctFilename):len(correctFilename)+intSize]))
                   
                    #newFileName = putDate(newFileName,magazine)
                    fixed = True
                elif regexfinalSS.search(newFileName): 
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
            extractCover(publishers[l]  , magazine , newFileName) 
            years = findYears(years,fulldate,newFileName)

        seekEpubConverts(magazine,newFileName)   
        missingRev += findMissing(magazine, fullList)
        totalRev  -= findDupes(magazine,fullList)  
       
        totalRev += len(fullList)
        if totalRev > 0 and missingRev > 0 :
            ##print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
            print("Total " + magazine + ": " + str(totalRev) + " Missing: " + str(missingRev) + " - "+  str("{:.3f}".format( 100* (totalRev/(missingRev+totalRev)))) + "% Completed ")
            missingMag.append(magazine)
        elif missingRev == 0:
            if publishers[l] != "web": 
                fullMag.append(magazine)     
        missingPub += missingRev
        totalPub += totalRev
        totalRev = 0 
        missingRev = 0
        fullList =[]
    if totalPub + missingPub >0 :
        formatted_float = "{:.3f}".format( 100* (totalPub/(missingPub+totalPub)))
        print("---------------Total: " + str(totalPub) + " Missing: " + str(missingPub) + " Complete: " + str(formatted_float) + "%")
    print("")
    total += totalPub
    missing += missingPub
if total + missing >0 : 
    formatted_float = "{:.3f}".format(100* (total/(missing+total)))    
    totalMags = (len(fullMag)) +  (len(missingMag))
    print("TOTAL ALL: " + str(total) + " MISSING ALL: " + str(missing) + " % COMPLETE ALL: " + str(formatted_float) + "%")
    print("TOTAL MAGAZINES: "+ str(totalMags) )
    print("COMPLETED MAGS: " + str(len(fullMag)) + ":"+ str(fullMag)) 
    print("PARTIAL MAGS: " + str(len(missingMag)) + ":" + str(missingMag))    
    printYears(years)
    printFullDate(fulldate)
    
input("Press Enter to continue...")

