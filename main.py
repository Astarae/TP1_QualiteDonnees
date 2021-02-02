#!/usr/bin/env python3

# from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.widgets as widgets
import numpy as np
from matplotlib.widgets import Button

month_array = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

#Lecture du fichier
def read_climat_file():
    """
    docstring
    """
    #Récupération des données du fichier Excel
    file = r'data/Climat.xlsx'
    dataClimatSI = pd.read_excel(file, sheet_name=0)

    totalTemperature = []
    for col in range (3, 15):
        month_temperature = []
        for row in range (3, 34):
            valueOfTemp = dataClimatSI.iloc[row, col]
            if(not np.isnan(valueOfTemp)):
                month_temperature.append(valueOfTemp)
        totalTemperature.append(month_temperature)
    return totalTemperature

def read_climat_file_for_annual_reading():
    """
    docstring
    """
    #Récupération des données du fichier Excel
    file = r'data/Climat.xlsx'
    dataClimatSI = pd.read_excel(file, sheet_name=0)

    totalTemperature = []
    for col in range (3, 15):
        month_temperature = []
        for row in range (3, 34):
            valueOfTemp = dataClimatSI.iloc[row, col]
            if(not np.isnan(valueOfTemp)):
                totalTemperature.append(valueOfTemp)
    return totalTemperature


#Lecture du second fichier
def read_climat_file_savukoski():
    """
    docstring
    """
    #Récupération des données du fichier Excel
    file = r'data/Savukoski kirkonkyla.xlsx'
    df = pd.read_excel(file, sheet_name=2)
    return df[df.columns[[1,2,5,6,7]]]

def read_climat_file_city_temperature(city):
    """
    docstring
    """
    #Récupération des données du fichier Excel
    file = r'data/city_temperature.csv'
    df = pd.read_csv(file, error_bad_lines=False, dtype={"Region": "string", "Country": "string", "State": "string", "City": "string", "Month": int, "Day": int, "Year": int, "AvgTemperature": float})
    df_tmp = df.loc[(df["City"] == city) & (df["Year"] == 2018)]
    return df_tmp[df_tmp.columns[[4,7]]]

def retrieve_all_day_per_month_for_city_temperature(df, city):
    annual_temps = []
    # month_temp = []
    for index in range(1, 13):
        df_tmp = df.loc[df["Month"] == index]
        for day_temp in df_tmp[df_tmp.columns[1]]:
            annual_temps.append((day_temp-32)  * (5.0/9.0))
    return annual_temps

def retrieve_year_temp_savu(df):
    annual_temps = []
    for index in range(1, 13):
        df_tmp = df.loc[df["m"] == index]
        for indice in range(len(df_tmp[df_tmp.columns[1]])):
            df_tmp_b = df_tmp.loc[df_tmp["d"] == indice+1]
            annual_temps.append(np.mean([df_tmp_b[df_tmp_b.columns[2]], df_tmp_b[df_tmp_b.columns[3]], df_tmp_b[df_tmp_b.columns[4]]])) 
    return(annual_temps)
    
#Calcul de la moyenne par mois
def retrieve_month_average(dataTemperature):
    """
    docstring
    """
    for month in range(len(dataTemperature)):
        temp_average = np.average(dataTemperature[month])
        print("Moyenne pour", month_array[month].upper() , ":", temp_average)


#Calcul de l'écart-type de chaque mois
def retrieve_month_deviation(dataTemperature):
    """
    docstring
    """
    print("#### Ecart-Type pour chaque mois ####")
    for month in range(len(dataTemperature)):
        temp_deviation = np.std(dataTemperature[month])
        print("Ecart-type pour", month_array[month].upper() , ":", temp_deviation)

#Calcul de la température maximale et minimale par mois
def retrieve_min_max_month(dataTemperature):
    """
    docstring
    """
    print("#### Températures maximales et minimales pour chaque mois ####")
    for month in range(len(dataTemperature)):
        temp_max = np.max(dataTemperature[month])
        temp_min = np.min(dataTemperature[month])
        print("Pour le mois de ", month_array[month].upper() , " la température minimale est : ", temp_min, "° et la température maximale est : ",  temp_max, "°")

#Calcul de la température maximale et minimale pour l'année
def retrieve_min_max_year(dataTemperature):
    """
    docstring
    """
    print("#### Température maximale et minimale pour l'année ####")
    lowest_year_temp = 0
    highest_year_temp = 0
    for month in range(len(dataTemperature)):
        temp_max = np.max(dataTemperature[month])
        temp_min = np.min(dataTemperature[month])
        if lowest_year_temp > temp_min:
            lowest_year_temp = temp_min
        if highest_year_temp < temp_max:
            highest_year_temp = temp_max
    print("Pour l'année, la température minimale est : ", lowest_year_temp, "° et la température maximale est : ",  highest_year_temp, "°")

#Générer des couleurs aléatoires
def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

#Création de graphiques pour chaque mois
def graph_month(dataTemperature):
    """
    docstring
    """
    cmap = get_cmap(len(dataTemperature))
    for month in range(len(dataTemperature)):
        plt.figure("Graphique des mois")
        plt.plot(dataTemperature[month], color=cmap(month))
        plt.xlabel("Jours")
        plt.ylabel("Température (°C)")
        plt.title(month_array[month])
        plt.grid()
        plt.show()

def comparaison_graph_annual_month():
    """
    docstring
    """
     
    array_si = read_climat_file_for_annual_reading()
    array_savukoski = retrieve_year_temp_savu(read_climat_file_savukoski())
    array_oslo = retrieve_all_day_per_month_for_city_temperature(read_climat_file_city_temperature("Oslo"), "Oslo")
    array_helsinki = retrieve_all_day_per_month_for_city_temperature(read_climat_file_city_temperature("Helsinki"), "Helsinki")
    array_reykjavik = retrieve_all_day_per_month_for_city_temperature(read_climat_file_city_temperature("Reykjavik"), "Reykjavik")
    array_stockholm = retrieve_all_day_per_month_for_city_temperature(read_climat_file_city_temperature("Stockholm"), "Stockholm")
    

    t = np.arange(1, 366, 1)
    fig, ax = plt.subplots()
    ax.set(xlabel='Jours', ylabel='Température (°C)',
        title='Graphique des températures')
    ax.plot(t, array_si, color='darkturquoise', label="SI")
    ax.plot(t, array_savukoski, color='deeppink', label="Savukoski")
    ax.plot(t, array_oslo, color='red', label="Oslo")
    ax.plot(t, array_stockholm, color='darkorange', label="Stockholm")
    ax.plot(t, array_reykjavik, color='darkviolet', label="Reykjavik")
    ax.plot(t, array_helsinki, color='green', label="Helsinki")
    ax.grid()
    ax.legend()
    # fig.savefig("screenshot/helsinki.png")
    # fig.savefig("screenshot/reykjavik.png")
    # fig.savefig("screenshot/savukoski.png")
    # fig.savefig("screenshot/stockholm.png")
    # fig.savefig("screenshot/comparaison.png")
    # fig.savefig("screenshot/oslo.png")
    plt.show()




#Création d'un graphique pour l'année
def graph_annual_month(dataTemperature):
    """
    docstring
    """
    flatten = lambda t: [item for sublist in t for item in sublist]

    class SnaptoCursor(object):
        def __init__(self, ax, x, y):
            self.ax = ax
            self.ly = ax.axvline(color='k', alpha=0.2) 
            self.marker, = ax.plot([0],[0], marker="o", color="darkorange", zorder=3, markersize=7) 
            self.x = x
            self.y = y
            self.txt = ax.text(0.7, 0.9, '')

        def mouse_move(self, event):
            if not event.inaxes: return
            x, y = event.xdata, event.ydata
            indx = np.searchsorted(self.x, [x])[0]
            x = self.x[indx]
            y = self.y[indx]
            self.ly.set_xdata(x)
            self.marker.set_data([x],[y])
            self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
            self.txt.set_position((x,y))
            self.ax.figure.canvas.draw_idle()
    
    t = np.arange(1, 366, 1)
    fig, ax = plt.subplots()
    cursor = SnaptoCursor(ax, t, flatten(dataTemperature))
    cid =  plt.connect('motion_notify_event', cursor.mouse_move)
    ax.set(xlabel='Jours', ylabel='Température (°C)',
        title='Graphique annuel')
    ax.plot(t, flatten(dataTemperature), color='darkturquoise')
    # fig.savefig("screenshot/graphAnnual.png")
    plt.show()
   



if __name__ == "__main__":
    #Fonction pour la moyenne de chaque mois
    retrieve_month_average(read_climat_file())
    print("\n")

    #Fonction pour la moyenne pour savukoski
    retrieve_year_temp_savu(read_climat_file_savukoski())
    print("\n")

    # Fonction pour l'écart-type de chaque mois
    retrieve_month_deviation(read_climat_file())
    print("\n")

    # Fonction pour la température maximale et minimale par mois
    retrieve_min_max_month(read_climat_file())
    print("\n")

    # Fonction pour la température maximale et minimale pour l'année
    retrieve_min_max_year(read_climat_file())
    print("\n")
    
    # Fonction pour le graphique de chaque mois
    graph_month(read_climat_file())

    # Fonction pour le graphique annuel 
    graph_annual_month(read_climat_file())

    # Fonction pour la comparaison des villes
    comparaison_graph_annual_month()
