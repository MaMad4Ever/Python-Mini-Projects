import os
from PyPDF2 import PdfReader

if not os.path.isdir("temp"):
    os.mkdir("temp")

inputPath = "./document.pdf"
outputPath = "./output.txt"

BASEDIR = os.path.realpath("temp")
print(BASEDIR)


if not outputPath:
    outputPath = os.path.join(BASEDIR, os.path.basename(inputPath).replace(".pdf", ".txt"))

with open(inputPath, 'rb') as pdfobj: 
    pdfread = PdfReader(pdfobj)
    num_pages = len(pdfread.pages)

    for i in range(num_pages):
        page = pdfread.pages[i]
        text = page.extract_text()
        if text:
            with open(outputPath, 'a+') as f:
                f.write(text)
