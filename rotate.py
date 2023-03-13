import PyPDF4

pdf_in = open('/Users/ghaz/documents/schoolwork/other/asian210/readings/Unthinking_Eurocentrism.pdf', 'rb')
pdf_reader = PyPDF4.PdfFileReader(pdf_in)
pdf_writer = PyPDF4.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(90)
    pdf_writer.addPage(page)

pdf_out = open('/Users/ghaz/documents/schoolwork/other/asian210/readings/UnthinkingEurocentrism.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()