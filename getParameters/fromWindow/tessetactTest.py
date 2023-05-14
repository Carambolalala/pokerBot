import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image = Image.open('test.png')
string = pytesseract.image_to_string(image, 'rus')
print(string)