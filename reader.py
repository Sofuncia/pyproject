import torch
import easyocr as ocr
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
import streamlit as st
from io import StringIO

def image_reader(image):
    # To read file as bytes:
    bytes_data = image.getvalue()
    reader = ocr.Reader(['uk'], gpu=False)
    result = reader.readtext(bytes_data)
    return result[0][1]







