import os
from os import walk
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

def get_pdf_list():
    r = []
    for (dirpath, dirnames, filenames) in walk("./input"):
        r.extend(filenames)
        break
    return r

canvas_width = 566
# Create the watermark from an image
c = canvas.Canvas('bin/sample-watermark.pdf')
c.drawImage('bin/logo.png', canvas_width - 500, 100, width=500, height=500,
            mask='auto', preserveAspectRatio=True)
c.drawString(canvas_width - 500, 12, "Downloaded from https://diplomate.greybits.in/")
c.save()

# large watermark sample for high res PDFs
# canvas_width = 566
# Create the watermark from an image
# c = canvas.Canvas('bin/sample-watermark--large.pdf')
# c.drawImage('bin/logo.png', canvas_width+int((canvas_width-1200)/2), 100, width=1200, height=1200,
#             mask='auto', preserveAspectRatio=True)
# c.drawString(canvas_width - 500, 12, "Downloaded from https://diplomate.greybits.in/")
# c.save()


right_pdf_list = get_pdf_list()

print("\nRIGHT PDFs : ")
for booklet_name in right_pdf_list:
    watermark = PdfFileReader(open("bin/sample-watermark.pdf", "rb"))
    output_file = PdfFileWriter()
    input_file = PdfFileReader(open("input/" + booklet_name, "rb"))
    page_count = input_file.getNumPages()

    # Go through all the left-watermarker file pages to add a watermark to them
    for page_number in range(page_count):
        print(booklet_name + ": Watermarking page {} of {}".format(page_number, page_count - 1))

        input_page = input_file.getPage(page_number)
        # setting a pdf scale to avoid creating different watermarks 
        input_page.scaleTo(width=612,height=792)

		# changing watermark according to PDF size 
        # print(list(input_page.mediaBox))
        # if list(input_page.mediaBox)[3] > 1500:
        # 	input_page.mergePage(large_watermark.getPage(0))
        # else:
        # 	input_page.mergePage(watermark.getPage(0))
        input_page.mergePage(watermark.getPage(0))
        output_file.addPage(input_page)
    if not os.path.exists("output"):
        os.mkdir("output")
    with open("output/" + booklet_name, "wb") as outputStream:
        output_file.write(outputStream)
