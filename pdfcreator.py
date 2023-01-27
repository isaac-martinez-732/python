import os, fitz , sys
from turtle import width

doc = fitz.open()  # PDF with the pictures
if len(sys.argv) == 1:
    print ("Editorial?")
    editorial = input()
    print ("Revista?")
    revista = input()
    print ("numeros?")
    numeros = input()   

else:
    editorial = sys.argv[1]
    if len(sys.argv) == 2:
        print ("Revista?")
        revista = input()
    else:
        revista = sys.argv[2]

imgdir = "F:\Portadas\\" + editorial + "\\" + revista  # where the pics are
imglist = os.listdir(imgdir)  # list of them
#imgcount = len(imglist)  # pic count
totalimages = 0
p = fitz.Point(50, 72)  # start point of 1st line
width = 952.5
height = 1312.5
k = 0
for i,f in enumerate(imglist):
    text = f[0:-4].replace(".png", "")
    page = doc.new_page(width = width,height = height)
    rc = page.insert_text(p,  # bottom-left of 1st char
                        text,  # the text (honors '\n')
                        fontname = "helv",  # the default font
                        fontsize = 25,  # the default font size
                        rotate = 0,  # also available: 90, 180, 270
                        )
    img = fitz.open(os.path.join(imgdir, f))  # open pic as document
    #new_image = img.resize((width, height))
    #new_image.save(text + ".jpg")
    rect = img[0].rect  # pic dimension
    pdfbytes = img.convert_to_pdf()  # make a PDF stream
    img.close()  # no longer needed
    imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
    
    #page = doc.new_page(width = width,height = height)
    page = doc.new_page(width = rect.width,  # new page with ...
                       height = rect.height)  # pic dimension
    page.show_pdf_page(rect, imgPDF, 0)  # image fills the page
    totalimages +=1
    k= k +1
    
    print( f + " added to pdf")
    if k > int(numeros) : break

doc.save("Portadas revista " + revista + " " +str(totalimages) + " numeros.pdf")