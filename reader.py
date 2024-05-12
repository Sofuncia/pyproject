import torch
import easyocr as ocr
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS



def split_lines(text):
    split_text = """"""
    for line in text.split("\n"):
        split_text += line + """
"""
    return split_text


def image_reader(image):
    reader = ocr.Reader(['uk'], gpu=False)
    result = reader.readtext(image)
    merged_text = ""
    full_text = """"""
    for i in range(len(result)):
        merged_text += result[i][1] + "\n"
        full_text = split_lines(merged_text)
    return full_text





