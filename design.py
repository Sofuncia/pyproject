import streamlit as st


class PageDetails:
    page_title = "Онлайн зчитувач тексту із зображення"  # details info on the page
    file_headline = "### Підтримувані типи файлів:"
    lang_headline = "### Підтримувані мови:"

    def __init__(self, file_types: list, lang_types: list):
        self.file_types = file_types  # for setting currently supported file extentions
        self.lang_types = lang_types  # and laguages
    
    @staticmethod
    def points(bullet_points):  # prints text in bullet point list
        for point in bullet_points:
            st.markdown(point)

    def show_details(self):  # prints all page details
        st.title(self.page_title)
        st.write(self.file_headline)
        self.points(self.file_types)
        st.write(self.lang_headline)
        self.points(self.lang_types)
        st.write("")

    