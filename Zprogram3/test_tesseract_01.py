from PIL import Image
import pytesseract

path = r"C:\Users\Wargon\Pictures\Saved Pictures\test_tesseract_01.png"


text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
