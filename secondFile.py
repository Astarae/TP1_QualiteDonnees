
#!/usr/bin/env python3

# from pandas import DataFrame, read_csv
from numpy.matrixlib import defmatrix
import pandas as pd
import numpy as np

month_array = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

#Lecture du fichier
def read_climat_file():
    """
    docstring
    """
    #Récupération des données du fichier Excel
    file = r'data/Savukoski kirkonkyla.xlsx'
    dataClimatSI = pd.read_excel(file, sheet_name=2)
    return dataClimatSI

#Calcul de la température maximale et minimale pour l'année
def retrieve_min_max_year(dataTemperature):
    """
    docstring
    """
    totalTemperature = []

    for col in range (7, 8):
        month_temperature = []
        for row in range (1, 366):
            valueOfTemp = dataTemperature.iloc[row, col]
            print(valueOfTemp)
            month_temperature.append(valueOfTemp)
        totalTemperature.append(month_temperature)
    print(totalTemperature)
    lowest_year_temp = 0
    highest_year_temp = 0
    for month in range(len(totalTemperature)):
        temp_max = np.max(totalTemperature[month])
        if highest_year_temp < temp_max:
            highest_year_temp = temp_max
    print("Pour l'année, la température maximale est : ",  highest_year_temp, "°")


if __name__ == "__main__":
    retrieve_min_max_year(read_climat_file())
