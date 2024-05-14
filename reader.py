import torch
import easyocr as ocr
import streamlit as st
import os
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
        st.code(full_text, language="python")



# def try_read_image(checked_file):
#     bytes_data = Image(checked_file.read())
#     recognized_text = bytes_data.read_image()


def is_file_type_supported(file):
    if file is not None:
        file_path = os.path.splitext(file)
        if (file_path[1] == ".jpg"
        or file_path[1] == ".png"
        or file_path[1] == ".tiff") is True:
            return True
        else:
            return False
    else: pass