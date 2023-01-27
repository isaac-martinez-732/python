import os
import sys
import filecmp 
import shutil
import re
from pathlib import Path
from filecmp import cmp
from os.path import isfile, join, isdir

def compare2dirs(path1, path2):
    result = filecmp.dircmp(path1, path2)
    movetodupes = list(set(result.same_files))  
    for duped in movetodupes:
        print(" dupes " + str(duped) )
        shutil.move(Path(path1) / duped , Path(path1) / "dupes" / duped)
        shutil.move(Path(path2) / duped , Path(path2) / "dupes" / duped)
    #result.report()

def compareFiles(path):
    DATA_DIR = Path(path)
    files = sorted(os.listdir(DATA_DIR))
    allfiles = len(files)
    print(allfiles)
    # List having the classes of documents
    # with the same content
    duplicateFiles = []
    movetodupes =[]
    i = 0
    # comparison of the documents
    for file_x in files:
        
        if_dupl = False
    
        for class_ in duplicateFiles:
            # Comparing files having same content using cmp()
            # class_[0] represents a class having same content
            if_dupl = cmp(
                DATA_DIR / file_x,
                DATA_DIR / class_[0],
                shallow=False
            )
            if if_dupl:
                class_.append(file_x)
                movetodupes.append( file_x)
                movetodupes.append(class_[0])
                print(" dupes " + str(file_x) + " and "+  str(class_[0]))
                break
    
        if not if_dupl:
            #print ("no dupes: " + file_x)
            duplicateFiles.append([file_x])
        i = i +1
        print ("{:.3%}".format(i/allfiles))

    # Print results
    #remove dupes in dupes
    movetodupes = list(set(movetodupes))  
    for duped in movetodupes:
        shutil.move(DATA_DIR / duped , DATA_DIR / "dupes" / duped)

def compareFilesSameName(path):
    DATA_DIR = Path(path)
    files = sorted(os.listdir(DATA_DIR))
    # List having the classes of documents
    # with the same content
    duplicateFiles = []
    
    # comparison of the documents
    for file_x in files:
    
        if_dupl = False
    
        for class_ in duplicateFiles:
            # Comparing files having same content using cmp()
            # class_[0] represents a class having same content
            if_dupl =   file_x == class_[0]
               
            if if_dupl:
                class_.append(file_x)
                f.write(" dupes " + file_x + " and "+ class_[0])
                print(" dupes " + str(file_x) + " and "+  str(class_[0]))
                break
    
        if not if_dupl:
            duplicateFiles.append([file_x])
    
    # Print results
    #print(duplicateFiles)

def basicFormat(newFileName):
    newFileName = newFileName.replace("nº", " ")
    newFileName = newFileName.replace("!", " ")
    newFileName = newFileName.replace("_", " ")
    newFileName = newFileName.replace("Â", "")
    newFileName = newFileName.replace("Ã", "")
    newFileName = newFileName.replace("°", "")
    newFileName = newFileName.replace("美", "") 
    newFileName = newFileName.replace("  ", " ")
    newFileName = newFileName.replace("{", "[")
    newFileName = newFileName.replace("}", "]")
    newFileName = newFileName.replace("@", " ")
    newFileName = newFileName.replace("~", " ")
    newFileName = newFileName.replace("件", " ")
    newFileName = newFileName.replace("克", " ")
    newFileName = newFileName.replace("兰", " ")
    newFileName = newFileName.replace("女", " ")
    newFileName = newFileName.replace("乌", " ") 
    newFileName = newFileName.replace("Ñ", "")
    ##newFileName = newFileName[0:-4].replace(".", " ") + newFileName[-4:]
    newFileName = newFileName[0].replace(" ", "") + newFileName[1:]
    newFileName = newFileName[0].replace("-", "") + newFileName[1:]
    newFileName = newFileName[0].replace("💋", "") + newFileName[1:]
    newFileName = newFileName[0].replace("+", "") + newFileName[1:]
    if newFileName.startswith("Los Simpson") :
        newFileName = newFileName.replace("[DVDRip ","")
        newFileName = newFileName.replace("Los Simpsons", "Los Simpson")
        newFileName = newFileName.replace("Los Simpson-", "Los Simpson ")
        newFileName = newFileName.replace("Los Simpson -", "Los Simpson ")
        regexOnly1digit = re.compile("^"+ "Los Simpson " + "[0-9]x")
        if regexOnly1digit.search(newFileName):
            newFileName = newFileName.replace("Los Simpson ", "Los Simpson 0")

    return newFileName

if  len(sys.argv) > 1:
    path =  sys.argv[1]
    dir = [sys.argv[1]]
else:
    path = os.getcwd() + "\\"
    dir = [f for f in os.listdir(path) if isdir(os.join(path, f))]


if not os.path.exists(path + "\dupes"): os.mkdir(path + "\dupes")

onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
fileList = []
for i in range(len(onlyfiles)):
    newFileName = basicFormat(onlyfiles[i])
    if onlyfiles[i] != newFileName:
        try:
            os.rename(path + "\\" + onlyfiles[i],path + "\\" + newFileName)
        except FileExistsError:
            ext = newFileName[-4]
            newFileName = newFileName.replace(ext, "(1)" + ext)
            try:
                os.rename(path + "\\" + onlyfiles[i],path + "\\" + newFileName)
            except FileExistsError:
                ext = newFileName[-4]
                newFileName = newFileName.replace(ext, "(1)" + ext)
    
    #print(newFileName + "-" + str(os.path.getsize(path + "\\" + newFileName)))

if  len(sys.argv) > 2:  compare2dirs( sys.argv[1], sys.argv[2])
else :
    compareFiles(path)
#compareFilesSameName(path)

