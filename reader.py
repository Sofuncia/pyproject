import torch
import easyocr as ocr
import streamlit as st
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS


class Image:
    def __init__(self, image):
        self.image = image

    def split_lines(text):
        split_text = """"""
        for line in text.split("\n"):
            split_text += line + """
    """
        return split_text

    def read_image(self):
        reader = ocr.Reader(['en','uk'], gpu=False)
        result = reader.readtext(self.image)
        merged_text = ""
        full_text = """"""
        for i in range(len(result)):
            merged_text += result[i][1] + "\n"
            full_text = self.split_lines(merged_text)
        return full_text
    
    def try_read_image(self):
        if self.image is not None:
            bytes_data = self.image.read()
            recognized_text = self.read_image(bytes_data)
            st.code(recognized_text, language="python")











