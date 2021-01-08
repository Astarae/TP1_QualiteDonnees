#!/usr/bin/env python

# from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.widgets as widgets
import numpy as np

month_array = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

#Maximum et minimum pour l'année
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
    temperature_global=[]

    file = r'data/Climat.xls'
    dataClimat = pd.read_excel(file, sheet_name=0)
    # for column in range (3, 15):
    #     month_temp=[]
    #     for row in range (3, 34):
    #         value_temp = dataClimat.iloc[row, column]
    #         if(not np.isnan(value_temp)):
    #             month_temp.append(value_temp)
    # temperature_global.append(month_temp)
    print(dataClimat)
    # return temperature_global

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

class SnaptoCursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([0],[0], marker="o", color="crimson", zorder=3) 
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

def graph_month(df):
    """
    docstring
    """
    for month_name in month_array:
        plt.figure(month_name)
        plt.plot(df[month_name])
        plt.xlabel("Jour du mois")
        plt.ylabel("Température")
        plt.title(month_name)
    return plt



def annual_month(df):
    # flatten = lambda t: [item for sublist in t for item in sublist]
    print (df)
    temperature = []

    for month_name in month_array:
        df[df[month_name] != 'NaN']
        for month_temp in df[df[month_name] != 'NaN'][month_name]:
            temperature.append(month_temp)

    # print(temperature)
    # t = np.arange(1, 366, 1)
    # # s = np.sin(2*2*np.pi*t)
    # fig, ax = plt.subplots()

    # cursor = SnaptoCursor(ax, t, temperature)
    # cid =  plt.connect('motion_notify_event', cursor.mouse_move)

    # ax.plot(t, temperature,)
    # plt.show()
    

    # plt.plot(temperature)
    # plt.ylabel("Température")
    # plt.xlabel("Jour de l'année")
    # plt.title("Moyenne Annuel")
    # plt.show()


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
    # annual_month(read_climat_file())
    read_climat_file()
    # annual_month()
