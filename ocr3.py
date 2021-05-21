import pytesseract
pytesseract.pytesseract.tesseract_cmd =
r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(r"C:\Users\PRAKASH\Desktop\sam.png")
f = open("recognized.txt", "a")
f.write(text)
f.close
