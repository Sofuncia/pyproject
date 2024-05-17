import torch
import easyocr as ocr
import streamlit as st
import os
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS


class Image:

    def __init__(self, file_to_check: list, image_in_bytes: str):
        self.file_to_check = os.path.splitext(file_to_check.name)
        self.image_in_bytes = image_in_bytes

    @staticmethod
    def split_lines(text):
        split_text = """"""
        for line in text.split("\n"):
            split_text += line + """
    """
        return split_text

    def read_image(self):
        reader = ocr.Reader(['en','uk'], gpu=True)
        result = reader.readtext(self.image_in_bytes)
        merged_text = ""
        full_text = """"""
        for i in range(len(result)):
            merged_text += result[i][1] + "\n"
            full_text = self.split_lines(merged_text)
        st.code(full_text, language="python")

    def is_file_type_supported(self):
        if (self.file_to_check[1] == ".jpg"
                or self.file_to_check[1] == ".jpeg"
                or self.file_to_check[1] == ".png"
                or self.file_to_check[1] == ".tiff") is True:
            return True
        else:
            return False