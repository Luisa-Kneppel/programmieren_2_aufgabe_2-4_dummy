import json
import pandas as pd
import plotly.express as px

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:
## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])
        self.df = self.df.iloc[:5000]  # Entferne die erste Zeile, da sie nur die Spaltennamen enthält
        self.peaks = []

    '''def plot_time_series(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        df_plot["is_peak"] = False
        df_plot.loc[self.peaks, "is_peak"] = True
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV", title="EKG Zeitreihe", color="is_peak")
        return self.fig'''

    def load_by_id(self, id): #Instanziiert einen EKG-Test anhand der ID und der Personen-Datenbank
        with open("data/person_db.json", "r", encoding="utf-8") as file: #erstmal die Personendatenbank öffnen
            person_data = json.load(file) #daten holen

        for person_dict in person_data: #durch die Personen durchgehen
            for ekg_test in person_dict["ekg_tests"]: #durch die ekg_tests der Person durchgehen
                if ekg_test["id"] == id: # ID des ekg_tests = der gesuchten ID, EKGdata Objekt mit diesem ekg_test
                    return EKGdata(ekg_test) # erstellt und zurückgegeben werden

        

    def find_peaks(self, threshold, respacing_factor=5):
        
        series = series = self.df["Messwerte in mV"] # die Spalte mit den EKG-Werten als Series speichern 
        series = series.iloc[::respacing_factor] # EKG-Daten ausdünnen
        series = series[series > threshold] # Nur Werte über dem Schwellwert behalten

        peaks = []
        last = 0
        current = 0
        next_value = 0

        for index, row in series.items():
            last = current
            current = next_value
            next_value = row

            if last < current and current > next_value and current > threshold:
                peaks.append(index - respacing_factor)

        self.peaks = peaks # Ergebnis als Attribut speichern

        return peaks

    def calculate_avg_hr(self, df):     # (df)
        df_peaks =df.loc[df["is peak"] == True]
        N_peaks = df_peaks["is_peak"].sum() # Anzahl der Peaks

        dt_ms = df_peaks["time in ms"].iloc[-1] - df_peaks["time in ms"].iloc[0] # Zeit in ms zwischen erstem und letztem Peak
        dt_min = dt_ms / (1000*60)
        avg_hr = N_peaks / dt_min # durchschnittliche Herzfrequenz in bpm
        return avg_hr


#die Abstände zwischen den Peaks und in Schläge pro Minute um.

    '''def plot(self):
        df_plot = self.df.copy() #damit wir den Dataframe nicht verändern

        df_plot["is_peak"] = False
        df_plot.loc[self.peaks, "is_peak"] = True

        fig = px.scatter(
            df_plot,
            x="Time in ms",
            y="EKG in mV",
            color="is_peak"
        )

        fig.show()'''

    def plot_time_series(self):
        df_plot = self.df.copy() #damit wir den Dataframe nicht verändern

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        df_plot["is_peak"] = False
        df_plot.loc[self.peaks, "is_peak"] = True
        self.fig = px.line(df_plot.head(2000), x="Zeit in ms", y="Messwerte in mV", title="EKG Zeitreihe", color="is_peak")
        return self.fig


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
    peaks = ekg.find_peaks(340)
    fig = ekg.plot_time_series()
    fig.show()

