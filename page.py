import streamlit as st
from reader import Image, is_file_type_supported
from design import PageDetails


page = PageDetails(["- JPG", "- PNG", "- TIFF"], ["- українська", "- англійська"])
page.show_details()


upload_file = st.file_uploader("Оберіть файл зображення")

if upload_file is not None:
    file_bytes = upload_file.read()
    if is_file_type_supported(file_bytes) is True:
        uploaded_file = Image(file_bytes)
    else: st.error("Тип обраного файлу не підтримується")
else: pass
