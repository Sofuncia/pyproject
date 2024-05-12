import streamlit as st
from reader import image_reader

st.title("First hello")
st.write("""### Hello hello!""")

uploaded_file = st.file_uploader("Choose a file")
# To read file as bytes:
bytes_data = uploaded_file.getvalue()
if uploaded_file:
    recognized_text = image_reader(bytes_data)
    st.code(recognized_text, language=python)