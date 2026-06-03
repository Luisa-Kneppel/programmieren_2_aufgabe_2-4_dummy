# implement all functions!
import pandas as pd
import numpy as np
import plotly.express as px

def read_data():
    df = pd.read_csv("data/activities/activity.csv", sep=",")
    df["time in seconds"] = np.arange(len(df))
    df["time in minutes"] = df["time in seconds"]/60
    return df

max_power = []

def find_best_power(df, windowsize_seconds, umrechnungsfaktor = 1): #das ... da muss noch etwas rein, weil windowsize hat die einheit sekunde, 
    #und hier muss irgendwie anzahl der zeilen/sekunde, sobald die zwei multipliziert werden, kürzt sich sekunde raus und 
    # übrig bleibt die anzahl (genau das brauchen wir hier)
    windowsize_rows = windowsize_seconds * umrechnungsfaktor

    rolling_mean = df["PowerOriginal"].rolling(windowsize_rows).mean()
    max_power = rolling_mean.max()

    return max_power

def find_all_windows(df, window_list, umrechnungsfaktor = 1):
    power_list = []
    for windowsize_seconds in window_list:
        best_power = find_best_power(df, windowsize_seconds, umrechnungsfaktor)
        power_list.append(best_power)
    df_power = pd.DataFrame({
        "time in seconds": window_list,
        "best_power": power_list
        })

    return df_power

def make_power_curve(df_power):
    fig = px.line(df_power, x= "time in seconds", y= "best_power")

    fig.update_xaxes(type="log")
    
    return fig

if __name__ == "__main__":
    df = read_data()
   # window_list = [10, 20, 30, 60, 120, 30, 1200, 3600, 7200]
    window_list = np.arange(1, 7201)
    df_power = find_all_windows(df, window_list)
    fig = make_power_curve(df_power)
    fig.show()

