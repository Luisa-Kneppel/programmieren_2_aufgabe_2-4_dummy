# implement all functions!
import pandas as pd
import numpy as np
import plotly.express as px

def read_data_for_power_curve():
    df = pd.read_csv("data/activities/activity.csv", sep=",")
    df["time in seconds"] = np.arange(len(df))
    df["time in minutes"] = df["time in seconds"]/60
    return df


'''umrechnungsfaktor= Messwerte pro Sekunde, 
z.B. 1 Messwert pro Sekunde, dann ist umrechnungsfaktor = 1, wir setzen ihn aber nicht fix auf 1, 
da es sonst zu Fehlern kommt, wenn die Abstände nicht genau 1 sekunde betragen => time_data'''

def find_best_power(power_data, time_data, windowsize_seconds): 

    # jetzt stellen wir sicher, dass die Funktion funktioniert, egal ob Series oder Array übergeben wird
    power_series = pd.Series(power_data)
    
    # Code flexibel für unregelmäßige Abstände machen: die Sekunden - Spalte wird in ein echtes Zeitformat für Pandas umgewandelt!
    # dh. durch das .index wird nicht mehr die Zeilennummer verwendet, sondern die echten Zeiten
    power_series.index = pd.to_timedelta(time_data, unit='s')    
    Zeitfenster = str(windowsize_seconds) + "s"     # Bsp. steht dann "3s"
    rolling_mean = power_series.rolling(Zeitfenster).mean()
    
    max_power = rolling_mean.max()

    return max_power

def find_all_windows(power_data, time_data, window_list):
    power_list = [] # leere Liste für die besten Leistungen der verschiedenen Fenstergrößen

    for windowsize_seconds in window_list: #geht die gewünschte Dauer durch
        #window list enhält die gewünschten Zeitpunkte in einer Liste

        best_power = find_best_power (power_data, time_data, windowsize_seconds)
        power_list.append(best_power)
    
    df_power = pd.DataFrame({           #das ist der gesuchte DataFrame, der die Zeitpunkte und die besten Leistungen enthält
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
    power_input = df["PowerOriginal"].to_numpy()
    # das .to_numpy wandelt es in ein reines numpy array um 
    # -> Funktion bekommt nicht gesamtes df, nur mehr die Zahlen daraus (macht es flexibel)
    time_input = df["time in seconds"].to_numpy()

    # wir brauchen die letzte/maximale Sekunde aus den Daten:
    maximal_seconds = int(time_input.max())
    window_list = np.arange(1, maximal_seconds + 1) # alle Sekunden von 1 bis max Dauer 


    df_power = find_all_windows(power_input, time_input, window_list)
    print(df_power[df_power["best_power"].diff() > 0])

    fig = make_power_curve(df_power)
    fig.show()

'''Für jede Dauer wird ein gleitender Durchschnitt berechnet, 
davon wird der Maximalwert genommen, und alle Maximalwerte zusammen ergeben die Power-Curve.'''