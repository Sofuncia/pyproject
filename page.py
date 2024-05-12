import streamlit as st
from reader import image_reader

st.title("Онлайн зчитувач тексту із зображення")
st.write("""### Підтримувані типи файлів:""")
st.markdown("- JPG")
st.markdown("- PNG")
st.markdown("- TIFF")


uploaded_file = st.file_uploader("Оберіть файл зображення")
bytes_data = uploaded_file.read()

if uploaded_file:
    recognized_text = image_reader(bytes_data)
    st.code(recognized_text, language="python")