import torch
import easyocr as ocr
import streamlit as st
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS


class Image:

    def __init__(self, image_in_bytes):
        self.image_in_bytes = image_in_bytes

    def split_lines(self, text):
        split_text = """"""
        for line in text.split("\n"):
            split_text += line + """
    """
        return split_text

    def read_image(self):
        reader = ocr.Reader(['en','uk'], gpu=False)
        result = reader.readtext(self.image_in_bytes)
        merged_text = ""
        full_text = """"""
        for i in range(len(result)):
            merged_text += result[i][1] + "\n"
            full_text = self.split_lines(merged_text)
        return full_text



def try_read_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = Image(uploaded_file.read())
        recognized_text = bytes_data.read_image()
        st.code(recognized_text, language="python")


