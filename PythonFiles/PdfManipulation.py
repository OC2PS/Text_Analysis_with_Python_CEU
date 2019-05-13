
#install third party module
import PyPDF2
import os

os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU/Input/pdfs")

WBL2019=open('app20170223.pdf', "rb")
reader=PyPDF2.PdfFileReader(WBL2019)
reader.numPages
page=reader.getPage(0)
p1=page.extractText()



file1=open('app20170223.pdf', "rb")
file2=open('app20170223.pdf', "rb")
reader1=PyPDF2.PdfFileReader(file1)
reader2=PyPDF2.PdfFileReader(file2)
writer=PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page=reader1.getPage(pageNum)
    writer.addPage(page)


for pageNum in range(reader2.numPages):
    page=reader2.getPage(pageNum)
    writer.addPage(page)
    
outputFile=open('../../Outputs/combined.pdf','wb')
writer.write(outputFile)

outputFile.close()
file1.close()
file2.close()