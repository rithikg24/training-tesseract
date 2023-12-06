try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract as tes

font="ocrb"         # Change according to the dataset

print(tes.image_to_string(Image.open("eng.ocrb.exp1.jpg"),lang=font))