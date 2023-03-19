import PyPDF4
from os import getcwd, path

pdf_in = open(path.join(input("Enter a file directory: "), input("Enter the file name: ")), 'rb')
pdf_reader = PyPDF4.PdfFileReader(pdf_in)
pdf_writer = PyPDF4.PdfFileWriter()


rotate_num: int = int(input("How much to rotate clockwise? "))
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    page.rotateClockwise(rotate_num)
    pdf_writer.addPage(page)

pdf_out = open(path.join(getcwd(), input("Enter an output file name: ")), 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()