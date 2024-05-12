import streamlit as st
from reader import image_reader

st.title("First hello")
st.write("""### Hello hello!""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write(image_reader(uploaded_file))