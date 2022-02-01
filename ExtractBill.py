import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import pikepdf

directory = input("Enter Bill Directory : ")
out_directory = input("Enter Output Directory : ")
pwd = input("Password : ")

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        input_pdf = pikepdf.open(f"{directory}/{filename}", password=pwd)
        dst = input_pdf.new()
        dst.pages.append(input_pdf.pages[0])
        dst.save(f"{out_directory}/{filename}")
