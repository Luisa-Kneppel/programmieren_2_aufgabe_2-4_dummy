import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from read_pandas import read_activity_csv
from read_pandas import mean_leistung
from read_pandas import max_leistung
from read_pandas import make_power_hr_plot
from read_pandas import add_zones
from read_pandas import make_zone_plot
from read_pandas import zone_statistics



# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")

    df = read_activity_csv()
    st.write("Mittlere Leistung:")
    st.write(mean_leistung(df))

    st.write("Maximale Leistung:")
    st.write(max_leistung(df))

    fig = make_power_hr_plot(df)
    st.plotly_chart(fig)

    max_hr = st.number_input("Maximale Herzfrequenz eingeben",
        min_value=100, max_value=250, value=200)
    # Eingabefeld für die max_hr mit Begrenzungen und einem Startwert als erste Angabe

    df = add_zones(df, max_hr) 
    #df hat alle Aktivitätsdaten und max_hr kommt aus dem Eingabefeld

    zone_fig = make_zone_plot(df)
    
    st.plotly_chart(zone_fig)


    stats = zone_statistics(df) #hier wird die Statistik erst nochmal berechnet aus der def
    st.write("Zeit und durchschnittiche Leistung pro Zone")
    st.dataframe(stats) # und hier wird die Berechnung dann in einer Tabelle angezeigt

