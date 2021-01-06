#!/usr/bin/env python

# from pandas import DataFrame, read_csv
import matplotlib.pyplot as pyplot
import pandas as pd
import matplotlib.widgets as widgets
import numpy as np

month_array = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

def find_lowest_and_max_temp(df):
    """
    docstring
    """ 
    lowest_year_temp = 0
    highest_year_temp = 0
    for month_name in month_array:
        df[df[month_name] != 'NaN']
        if lowest_year_temp > df[month_name].min():
            lowest_year_temp = df[month_name].min()
        if highest_year_temp < df[month_name].max():
            highest_year_temp = df[month_name].max()
    print(lowest_year_temp)
    print(highest_year_temp)

def read_climat_file():
    """
    docstring
    """
    file = r'data/Climat.xls'
    df = pd.read_excel(file, sheet_name=0)
    return df

#Ecart type par mois
def retrieve_month_deviation(df, month_name):
    """
    docstring
    """
    df[df[month_name] != 'NaN']
    print("Ecart-type pour", month_name.upper(), ":", df[month_name].mean())

#Moyenne par mois
def retrieve_month_average(df, month_name):
    """
    docstring
    """
    df[df[month_name] != 'NaN']
    print("Moyenne pour", month_name.upper(), ":", df[month_name].std())


#Maximum et minimum pour l'année
def retrieve_max_year(self, parameter_list):
    """
    docstring
    """

#Maximum et minimum pour chaque mois
def retrieve_min_max_month(df, month_name):
    """
    docstring
    """
    df[df[month_name] != 'NaN']
    print("Pour", month_name.upper(), "le min est à", df[month_name].min(), "° et le max est à", df[month_name].max(), "°")

def read_coordinates():
    file = r'data/Savukoski kirkonkyla.xls'
    data = pd.read_excel(file)
    return data

def graph_month(df):
    """
    docstring
    """
    for month_name in month_array:
        pyplot.figure(month_name)
        # pyplot.plot(df[month_name])
        # pyplot.xlabel("Jour du mois")
        # pyplot.ylabel("Température")
        # pyplot.title(month_name)

       fig, ax = pyplot.subplots()
        ax.plot(df[month_name])
        pyplot.xlabel("Jour du mois")
        pyplot.ylabel("Température")
        pyplot.title(month_name)
        cursor = SnaptoCursor(ax)
    fig.canvas.mpl_connect('motion_notify_event', cursor.mouse_move)

#     fig, ax = plt.subplots()

# cursor = SnaptoCursor(ax, t, flatten(temperature))
# cid =  plt.connect('motion_notify_event', cursor.mouse_move)

# ax.plot(t, flatten(temperature),)
# plt.show()

    return pyplot



def annual_month(df):
    # flatten = lambda t: [item for sublist in t for item in sublist]
    temperature = []

    for month_name in month_array:
        df[df[month_name] != 'NaN']
        for month_temp in df[df[month_name] != 'NaN'][month_name]:
            temperature.append(month_temp)
            
        
    print(temperature)
    pyplot.plot(temperature)
    pyplot.ylabel("Température")
    pyplot.title("Moyenne Annuel") 
    pyplot.show()


if __name__ == "__main__":
    # print("#### Moyenne ####")
    # for month in month_array:
    #     retrieve_month_average(read_climat_file(), month)
    #     pass
    # print("\n")

    # print("#### Ecart-Type ####")
    # for month in month_array:
    #     retrieve_month_deviation(read_climat_file(), month)
    #     pass   
    # print("\n")
    
    # print("#### Min Max par Mois ####")
    # for month in month_array:
    #     retrieve_min_max_month(read_climat_file(), month)
    #     pass   
    # print("\n")
    
    # print("#### Min Max year ####")
    # find_lowest_and_max_temp(read_climat_file()) 
    # print("\n")

    # graph_month(read_climat_file()).show()
    # graph_month()
    annual_month(read_climat_file())
