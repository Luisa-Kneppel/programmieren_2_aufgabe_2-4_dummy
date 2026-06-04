# implement all functions!
import pandas as pd
import numpy as np
import plotly.express as px

def read_data():
    df = pd.read_csv("data/activities/activity.csv", sep=",")
    df["time in seconds"] = np.arange(len(df))
    df["time in minutes"] = df["time in seconds"]/60
    return df


'''umrechnungsfaktor= Messwerte pro Sekunde, 
z.B. 1 Messwert pro Sekunde, dann ist umrechnungsfaktor = 1'''

def find_best_power(df, windowsize_seconds, umrechnungsfaktor = 1): 
    # windowsize hat die Einheit Sekunde
    # Umrechnungsfaktor hat die Einheit Messwerte pro Sekunde
    # beides multiplizieren, damit wir die Anzahl der Zeilen bekommen
    # Anzahl brauchen wir für das rolling mean

    windowsize_rows = int(windowsize_seconds * umrechnungsfaktor)
    #Festergröße in sekunden wird in eine Festergröße in Zeilen umgerechnet
    # int, da wir nur ganzahlige Zeilen haben können

    rolling_mean = df["PowerOriginal"].rolling(windowsize_rows).mean()
    max_power = rolling_mean.max()

    return max_power

def find_all_windows(df, window_list, umrechnungsfaktor = 1):
    power_list = [] # leere Liste für die besten Leistungen der verschiedenen Fenstergrößen

    for windowsize_seconds in window_list: #geht die gewünschte Dauer durch
        #window list enhält die gewünschten Zeitpunkte in einer Liste

        best_power = find_best_power(df, windowsize_seconds, umrechnungsfaktor)

        power_list.append(best_power)
    
    df_power = pd.DataFrame({
        "time in seconds": window_list,
        "best_power": power_list
        })

    df_power = df_power.dropna() #ungültige Werte entfernt die Nan ausgeben

    df_power["best_power"] = df_power["best_power"].cummin()
    # die anstiege in der Leistungskurve entfernen, da sie nicht realistisch sind,
    # sondern nur durch Messfehler entstehen können

    return df_power

def make_power_curve(df_power):

    fig = px.line(
        df_power, 
        x= "time in seconds", 
        y= "best_power", 
        title="Power Curve",
        labels={"time in seconds": "Zeit in Sekunden ", "best_power": "Leistung in Watt "}
    )

    tick_values = [1, 2, 5, 10, 30, 60, 120, 300, 600, 1200, 3600, 7200]
    tick_text = ["0:01", "0:02", "0:05", "0:10", "0:30", "1:00", "2:00", 
                 "5:00", "10:00", "20:00","1:00:00", "2:00:00"]
    #tick ist einfach Strich auf der Achse und ticktext ist die Beschriftung dieses Strichs

    fig.update_xaxes(
        type="log", tickvals=tick_values, ticktext=tick_text,
        title="Zeit", showgrid=True, gridcolor="lightgray")
    # tickvals ist Befehl, wo die Striche auf der x-Achse sein sollen,
    # ticktext ist Befehl, wie die Beschriftung dieser Striche sein soll

    fig.update_yaxes(
        title="Leistung in Watt",showgrid=True, gridcolor="lightgray")

    fig.update_traces(line=dict(width=3))


    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white")
    return fig

if __name__ == "__main__":
    df = read_data()
    window_list = np.arange(1, len(df))
    df_power = find_all_windows(df, window_list)
    print(df_power[df_power["best_power"].diff() > 0])
    # test ob es steigungen in der Leistungskurve gibt, wollen wir nicht
    #print(df_power)
    fig = make_power_curve(df_power)
    fig.show()

