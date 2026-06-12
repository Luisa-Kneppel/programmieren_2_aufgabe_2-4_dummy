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

![Screenshot](/screenshot_Abgabe-3_Bild2.png)
![Screenshot](/screenshot_Abgabe-3_Bild1.png)

In der 4. Aufgabe haben wir unsere bisherigen Codes mit neuen Modulen erweitert,um eine übersichtliche und verständliche App zu gestallten.
Zuerst haben wir die Module person.py und ekgdata.py entwickelt. Person.py lädt Personendaten aus der Datei data/person_db.json und erstellt daraus Objekte der Klasse Person. Jedes Objekt der Klasse enthält die personenbezogene Informationen.
In der Funktion get_person_data() werden alle Personen als Liste zurückgegeben und über get_person_object_by_full_name() anhand von  "Nachname, Vorname" gesucht.
Ekgdata lädt EKG-Messdaten und speichert sie in einem DataFrame. Die Klasse EKGdata instanziiert einen EKG-Test (mit der ID) inload_by_id und sucht mit der Methode find_peaks, Peaks in den EKG-Daten und  berechnet mit avg_hr daraus die durchschnittliche Herzfrequenz. Mit plot_time_series() wird die EKG-Zeitreihe daraufhin dargestellt. Dabei werden die Messwerte über der Zeit geplottet und die erkannten Peaks werden zusätzlich als rote Punkte markiert, damit die Ausschläge im EKG-Signal direkt sichtbar sind.