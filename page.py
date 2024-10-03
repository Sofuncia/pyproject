import streamlit as st
from reader import Image
from design import PageDetails


page = PageDetails(["- JPG", "- PNG", "- TIFF"], ["- українська", "- англійська"])
page.show_details()  # prints page details


upload_file = st.file_uploader("Оберіть файл зображення")  # sets a block for uploading files

if upload_file is not None:
    alr_uploaded_file = Image(upload_file, upload_file.read())  # extension name and file in bytes
    if alr_uploaded_file.is_file_type_supported() is True:
        alr_uploaded_file.read_image()  # reads the already uploaded file
    else: st.error("Тип обраного файлу не підтримується")  # error message file type not supported
else: pass
