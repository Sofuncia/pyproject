import torch
import easyocr as ocr
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS



def image_reader(image):
    reader = ocr.Reader(['uk'], gpu=False)
    result = reader.readtext(image)
    if len(result) > 1:
        full_text = ""
        for i in range(len(result)):
            print(full_text)
            full_text += result[i][1] + "\n"
        return full_text[0]
    else: return result[0][1]





