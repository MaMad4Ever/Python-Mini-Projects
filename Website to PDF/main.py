import pdfkit

website_link = "www.google.com"

pdf_output = "output.pdf"

pdfkit.from_url(website_link,pdf_output)
