import streamlit as st
from reader import Image
from design import PageDetails


page = PageDetails(["- JPG", "- PNG", "- TIFF"], ["- українська", "- англійська"])
page.show_details()


upload_file = st.file_uploader("Оберіть файл зображення")

if upload_file is not None:
    alr_uploaded_file = Image(upload_file, upload_file.read())
    if alr_uploaded_file.is_file_type_supported() is True:
        alr_uploaded_file.read_image()
    else: st.error("Тип обраного файлу не підтримується")
else: pass
