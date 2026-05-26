import streamlit as st
import read_data 
from PIL import Image

person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)

st.write("# EKG APP")

col1, col2 = st.columns(2)
with col1:
    st.header("Versuchsperson auswählen")

    current_user = st.selectbox(
        'Versuchsperson',
        options = person_names, key="sbVersuchsperson")
    
    if current_user in person_names:
        picture_path = read_data.find_person_data_by_name(current_user)["picture_path"]
    
    st.write("Der Name ist:", current_user)
    st.write("Der Pfad ist:", picture_path)

with col2:
    st.image(Image.open(picture_path), caption=current_user)
    