import streamlit as st
import os
# from reader import read_image
from reader import try_read_image
from design import PageDetails

# st.title("Онлайн зчитувач тексту із зображення")
# st.write("### Підтримувані типи файлів:")
# st.markdown("- JPG")
# st.markdown("- PNG")
# st.markdown("- TIFF")

# st.write("### Підтримувані мови:")
# st.markdown("- українська")
# st.markdown("- англійська")
# st.write("")

page = PageDetails(["- JPG", "- PNG", "- TIFF"], ["- українська", "- англійська"])
page.show_details()


upload_file = st.file_uploader("Оберіть файл зображення")



file_name, file_extention = os.path.splitext(upload_file.name)
if (file_extention == ".jpg"
    or file_extention == ".png"
    or file_extention == ".tiff") is True:
    try_read_image(upload_file)
else: st.error("Тип обраного файлу не підтримується")

# uploaded_file = Image(upload_file)
# uploaded_file.try_read_image()
