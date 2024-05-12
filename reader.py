import torch
import easyocr as ocr
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

def image_reader(image):
    reader = ocr.Reader(['uk'], gpu=False)
    result = reader.readtext(image)
    return result[0][1]






