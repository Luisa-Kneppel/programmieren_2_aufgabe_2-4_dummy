import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import read_data 
from PIL import Image
from person import get_person_data, get_person_object_by_full_name
from ekgdata import EKGdata


person_objects = get_person_data()
person_names = []
for person in person_objects:
    name = person.get_full_name()
    person_names.append(name)

st.write("# EKG APP")

col1, col2 = st.columns(2)
with col1:
    st.header("Versuchsperson auswählen")

    current_user = st.selectbox(
         'Versuchsperson',
         options = person_names, key="sbVersuchsperson")
    
    person = get_person_object_by_full_name(current_user)

    if person: # sicherstellen dass sie existiert, bevor man Daten abfragen kann

        st.write("Der Name ist:", current_user)
        st.write("Der Pfad ist:", person.picture_path)

with col2:
    if person:
        st.image(person.get_image(), caption = current_user)

if person:
    st.header("EKG Analyse")

    if len(person.ekg_tests) > 0:
        test_Auswahl = []
        
        # Durch alle EKG-Tests der ausgewählten Person gehen
        for t in person.ekg_tests:
            test_text = t['date']    # Benennt die Optionen die zur Auswahl stehen
            test_Auswahl.append(test_text)
            
        selected_test = st.selectbox("Wähle einen EKG-Test aus:", options=test_Auswahl)     # Auswahlfeld in Streamlit einbauen

        test_index = test_Auswahl.index(selected_test)
        ekg_test = person.ekg_tests[test_index]

        ekg = EKGdata(ekg_test)
        threshold = 340
        ekg.find_peaks(threshold)
        herzfrequenz = ekg.estimate_hr()
        fig = ekg.plot_time_series()
        st.write("Die Herzfrequenz beträgt:", herzfrequenz, "bpm")
        st.plotly_chart(fig)    #, use_container_width=True

    else:
        st.warning("Für diese Person gibt es in der Datenbank keine EKG-Tests.")
