
from asyncio.windows_events import NULL
from fileinput import filename
import os  

from os.path import isfile, join, isdir

##START SCRIPT
initialYear = 1984
finalYear = 2023
yearsRange = finalYear - initialYear +1
table = "<html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><style>"
table += "img {   border: 1px solid #ddd;   border-radius: 4px;  padding: 5px;   width: 150px; }"
table +=" img:hover {  box-shadow: 0 0 2px 1px rgba(0, 160, 212, 0.5);}"
table +=" body {  background-image: url(\"../paper.jfif\");}"
table +="</style></head><body>"
table += "<table>\n"

months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

path = os.getcwd() + "\\"
publishers = [f for f in os.listdir(path) if isdir(join(path, f))]
years = [0] * (yearsRange)

def createParentHtml(years):
    total = 0
    yearsIndex = 0
    fileout = open( "web/parent.html", "w")
    newTable = table
    newTable += "<tr>\n"
    for i in range(len(years)):
        year =str(initialYear+i) 
        if yearsIndex > 9 : 
            newTable += "</tr>\n"
            newTable += "<td><a href=\""+ year + "/" +year+".html\">"+year+"</a></td><td>" + str(years[i]) + "</td>"
            yearsIndex = 0
        else:
            newTable += "<td><a href=\""+ year + "/"+year+".html\">"+year+"</a></td><td>" + str(years[i]) + "</td>"
        yearsIndex += 1 
        total += years[i]
    newTable += "<tr><td>Total Revistas : " + str(total)+ "</td></tr>"
    fileout.writelines(newTable)    
    fileout.close()  

def createYearsHtml(years):
    
    fulldate = [[0]*len(months) for i in range(yearsRange)]
    newTable = table
    magazinesList = []
    coverList = []
    fileList = []

    for y in range(len(fulldate)):
        year =str(initialYear+y) 
        nextYear = initialYear+y +1
        pastYear = initialYear+y -1
        if not os.path.exists(path + "/web/"+ year): os.mkdir(path + "/web/"+  year)
        fileout = open( "web/" + year + "/" + year + ".html", "w")
        newTable += " <tr><td><h1>Revistas del " + year + "</h1></td>"
        newTable += "<td></td><td><a href=\"../parent.html\">Inicio</a></td>"
        if pastYear >= initialYear :
            newTable += "<td></td><td><a href=\"../" +str(pastYear) +"/" + str(pastYear) +  ".html\">" + str(pastYear)+ "</a></td>"
        if nextYear <= finalYear :
            newTable += "<td></td><td><a href=\"../" +str(nextYear) +"/" + str(nextYear) +  ".html\">" + str(nextYear)+ "</a></td>"
        newTable += "</tr>"
        newTable += "<tr>\n"
        for m in range(len(fulldate[y])):
            newTable += "<td><a href=\""+months[m]+year+".html\">Revistas de "+months[m] +" del " +year+"</a></td>"
            for l in range(len(publishers)):
                if len(publishers) == 1 : publisherDir = path   
                else :  publisherDir = path   + "\\" + publishers[l]
                onlyDirs = [f for f in os.listdir(publisherDir ) if isdir(join(publisherDir, f))]
                for k in range(len(onlyDirs)):
                    magazine = onlyDirs[k]
                    subdir = publisherDir + "\\" + magazine
                    onlyfiles = [f for f in os.listdir(subdir) if isfile(join(subdir, f))]
                    for i in range(len(onlyfiles)):
                        revista = onlyfiles[i]
                        magazinesList,coverList = findDates(magazinesList,coverList, fileList, months[m],year,revista,magazine,publishers[l] )
            years[y] += len(magazinesList)
            newTable += "<td>Total Revistas: " + str(len(magazinesList))+  "</td></tr>\n"
            print("crear html " + months[m] + year)
            createMonthHtml(magazinesList,coverList,fileList,months[m], year)
            magazinesList = []
            coverList = []
            fileList = []
        fileout.writelines(newTable)    
        fileout.close()
        newTable = table
    return years

def findDates(lista,coverList,fileList,month,year,fichero,revista,editorial):
    portada = "F:/Portadas/"
    if fichero.lower().find("pdf")  > -1 :
        if fichero.lower().find(month) > -1:
            if fichero.find(year) > -1: 
                portada += editorial + "/" + revista + "/" +  fichero.replace(".pdf", ".png")
                fileList.append("f:/Revistas Retro/"  + editorial + "/" + revista + "/" +  fichero)
                coverList.append(portada)
                fichero = fichero.replace(".pdf", "")            
                fichero = fichero.replace(month, "")
                fichero = fichero.replace(" de", "")
                fichero = fichero.replace(month[0].upper()+ month[1:], "")
                fichero = fichero.replace(year, "")
                fichero = fichero.replace("-", "")
                lista.append(fichero)
    return lista ,coverList

def nextMonth(month,year):
    newmonth = ""
    newyear = 0
    for i in range(len(months)):
        if months[i] == month and i < 11: 
            newmonth  = months[i+1] 
            newyear = year
        elif months[i] == month and i == 11: 
            newmonth  = months[0]
            newyear = int(year) + 1 
    return newmonth,newyear

def previousMonth(month,year):
    newmonth = ""
    newyear = 0
    for i in range(len(months)):
        if months[i] == month and i > 0: 
            newmonth  = months[i-1] 
            newyear = year
        elif months[i] == month and i == 0: 
            newmonth  = months[11]
            newyear = int(year) - 1 
    return newmonth,newyear

def capitalize(word):
    newword = word[0].upper()+ word[1:]
    return newword

def createMonthHtml(magazinesList,coverList,fileList, month,year):
    fileout = open( "web/" +year + "/" + month +year + ".html", "w")
    newmonth,newyear = nextMonth(month,year)
    pastmonth,pastyear = previousMonth(month,year)
    newTable = table
        # Create the table's column headers
    header = " Revistas de " +capitalize(month) + " del " + year
    newTable += "  <tr>\n"
    newTable += "    <th><h1>{0}</h1></th>\n".format(header)
    newTable += "<td></td><td></td><td></td><td><a href=\"../"+ str(pastyear) + "/"+pastmonth+str(pastyear)+".html\">Revistas de "+capitalize(pastmonth) +" del " +str(pastyear)+"</a></td>"
    newTable += "<td><a href=\"../"+ str(newyear) + "/"+newmonth+str(newyear)+".html\">Revistas de "+capitalize(newmonth) +" del " +str(newyear)+"</a></td>"
    newTable += "<td></td><td><a href=\"../"+year + "/"+year+".html\">Revistas del " +year+"</a></td>"
    newTable += "<td></td><td><a href=\"../parent.html\">Inicio</a></td>"
    newTable += " </tr>"
    newTable += "  <tr>\n"
    magazineIndex  = 0
    # Create the table's row data
    for line in range(len(magazinesList)):
        subtable = "<td><a href=\"file:///{1}\" target=\"_blank\">{0}</a></td>\n".format(magazinesList[line].strip(),fileList[line])
        subtable += "<td><a target=\"_blank\" href=\""+ coverList[line]  + "\"><img src=\""+coverList[line] + "\" alt=\"{0}\"> </a></td>\n".format(magazinesList[line].strip())
        
        if magazineIndex > 2 : 
            newTable += " </tr>\n"
            newTable += subtable
            magazineIndex = 0         
        else: 
            newTable += subtable
        magazineIndex += 1
    newTable += "</tr>\n"
    newTable += "</table>"
    fileout.writelines(newTable)
    fileout.close()

years = createYearsHtml(years)
createParentHtml(years)
    
input("Press Enter to continue...")