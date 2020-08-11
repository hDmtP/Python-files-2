import img2pdf
from PIL import Image
import os

img_path = r"C:\Users\user\OneDrive\Python real life projects\img.jpg"
pdf_path = r"C:\Users\user\OneDrive\Python real life projects\img.pdf"

image = Image.open(img_path)
pdf_bytes = img2pdf.convert(img.jpg)

file = open(pdf_path, 'wb')
file.write(pdf_bytes)

image.close()
file.close()

print("Successfully converted to pdf")