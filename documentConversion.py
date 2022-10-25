#Joshua Mandell
#10/25/2022
#Document Conversion code for first AWS assignment

import aspose.words as aw
import os

def convertDoc (document, outform): #input: 'document' is path to .pdf document. 'outform' is the file extension.
    doc = aw.Document(document)
    doc.save(document.split(".")[0] + outform)
    
def test_pdfToRTF ():
    os.chdir("C:/Users/joshu/Dropbox/Data Science Graduate Program/Brandeis - Master's Strategic Analytics/RSEG 176/Assignment 1/RSEG-176-Assignment-1") #obviously change to whatever your working directory is.
    convertDoc("example_pdf_syllabus.pdf", ".rtf")
    
def test_rtfToDocx():
    convertDoc("example_pdf_syllabus.rtf", ".docx")
    
#JM 10/25/2022: tested both of the 'test' methods to make sure they work at creating new files. They do work - copying all the pdf text. However, there is a watermark (in the form of red text on the first page) added by aspose.words
    #TODO use file manipulation to remove the watermark after creating the file?
#Also, note, this was tested with a pdf with searchable text. If using a pdf without searchable text, unsure if the conversion would work properly. OCR may be necessary as an intervention (perhaps more ambitious than required for our minimum viable prototype)