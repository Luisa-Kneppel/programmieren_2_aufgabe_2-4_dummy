import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import read_data 
from PIL import Image

from advanced_power_curve import find_all_windows
from advanced_power_curve import make_power_curve
from advanced_power_curve import read_data_for_power_curve

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

#Implementierung der Power-Curve

df = read_data_for_power_curve()
power_input = df["PowerOriginal"].to_numpy()
time_input = df["time in seconds"].to_numpy()

maximal_seconds = int(time_input.max())
window_list = np.arange(1, maximal_seconds + 1) 

df_power = find_all_windows(power_input, time_input, window_list)
print(df_power.head()) #anzeigen der ersten 5 Zeilen des DataFrames

fig = make_power_curve(df_power)
fig.show()