from pdf2docx import Converter

pdf_file = "document.pdf"
docx_file = "document.docx"

cv = Converter(pdf_file)

cv.convert(docx_file)

cv.close()
