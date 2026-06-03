# Programmieren_2_aufgabe_2-4
This repository is used for exercise 2 - 4 of the programming lecture. This project is done by Johanna Helfer and Luisa Kneppel. 
Zu Beginn haben wir das Hauptmodul „interactive plot.py“ erstellt und streamlit importiert.
In einem Nebenmodul („read_pandas.py“) haben wir die Pakete Pandas, Plotly und Numpy importiert, sowie verschiedene Funktionen zur Berechnung und grafischen Darstellung definiert:
- read_my_csv() und read_activity_csv() werden genutzt um die Daten aus „ekg_data“ und „activity.csv“ einzulesen, beide Dateien sind unter „data“ abgelegt. 
- make_plot erstellt einen Line Plot, der die ersten 2000 Werte mit der Zeit in Millisekunden abbildet.
- Mit make_power_hr_plot wird ein Line Plot erstellt, der die Leistung sowie die Herzfrequenz über die Zeit in Minuten anzeigt.
- add_zones teilt die Herzfrequenz basierend auf den prozentualen Anteilen der maximalen Herzfrequenz in fünf Zonen ein.
- make_Zone_plot: um die Streamlit App übersichtlicher zu gestalten, haben wir die Herzfrequenzzonen in einem zusätzlichen Plot abgebildet, die einzelnen Zonen werden dabei mit verschiedenen Farben dargestellt. 
In separaten Funktionen wird die durchschnittliche- sowie die maximale Leistung berechnet. Um die verbrachte Zeit und die durchschnittliche Leistung pro Zone anzuzeigen, haben wir durch die Funktion zone_statistics eine Tabelle erzeugt, in der die Werte gegenübergestellt werden.
Nachdem die Funktionen auf ihre Richtigkeit geprüft haben, haben wir sie in unser Hauptmodul „ interactive_plot.py“ implementiert. 
Die Streamlit App wird in zwei Tabs unterteilt: „EKG – Data“ und „Power – Data“. Im ersten Tab wird die EKG – Visualisierung gezeigt. Im zweiten Tab wird zu Beginn die berechnete mittlere und maximale Leistung angezeigt. Darunter wird der Verlauf von Leistung und Herzfrequenz abgebildet. Über ein interaktives Eingabefeld kann der Nutzer seine maximale Herzfrequenz eingeben, daraufhin wird die Zonen – Verteilung berechnet, im Diagramm dargestellt sowie die statistische Auswertung angezeigt.
Um die Streamlit App zu starten, muss im Terminal „streamlit run interactive_plot.py“ eingegeben werden und mit Enter bestätigt werden. 

![Screenshot](/screenshot.png)