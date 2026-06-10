import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import read_data 
from PIL import Image

#import person.py
#import ekgdata.py 



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



from person import get_person_data
from ekgdata import EKGdata


def analyse_ekg(person_index, ekg_index, threshold): #indexe für die Auswahl der Person und des EKG-Tests
    persons = get_person_data() 

    selected_person = persons[person_index] #Person anhand des Index auswählt
    selected_ekg_test = selected_person.ekg_tests[ekg_index] #EKG-Test anhand des Index auswählt, wie person

    ekg = EKGdata(selected_ekg_test) # ekg als Objekt erstellen

    ekg.find_peaks(threshold) #wieder peaks finden aber nun individuell aus dem Test

    fig = ekg.plot_time_series() #plotten

    return selected_person, ekg, fig 

'''def main(): --> Testblock
    selected_person, ekg, fig = analyse_ekg( 
        person_index=0,
        ekg_index=0,
        threshold=340
    )

    print("Ausgewählte Person:")
    print(selected_person.get_full_name())

    print("EKG-ID:")
    print(ekg.id)

    print("Anzahl Peaks:")
    print(len(ekg.peaks))

    fig.show()'''