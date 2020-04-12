'''
PyPDF2 can extract only text and not images from PDF
'''
import PyPDF2

# opening PDF in rb - read binary mode since PDFs are binary files
pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)
print("Number of pages")
print(reader.numPages)

page = reader.getPage(0)
print("Read Text from First page")
print(page.extractText())

print("Reading Over all the pages")
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    print(page.extractText())

pdfFile.close()

'''
PyPDF2 can't write arbitrary text to PDF like python on can do with plain text files because of the
complex file format for PDF documents, it is limited to editing content at the page level.
You can add pages, remove pages, reorder pages in a PDF but you can't change the individual text on a
particular pageor change the color or font  or any of the layout
'''

# let's try to add PDF page from one PDF to the other

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()

'''
SO we can see that we can't create PDF docs from scratch but we can use other PDF docs to create a new one
'''