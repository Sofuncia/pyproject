import torch
import easyocr as ocr
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

def image_reader(image):
    reader = ocr.Reader(['uk'], gpu=False)
    result = reader.readtext(image)
    if len(result) > 1:
        for i in result:
            full_text += result[i][1] + "\n"
        return full_text[0]
    else: return result[0][1]





