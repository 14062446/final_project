from NetMatrixBuild import *
from DataClean import *
'''
Authors: Alex Simonoff and Nora Barry

This module contains functions used to merge weather data with our station data.

'''

def mergeWeatherData(weatherData, citiBikeData):
    '''This function takes in two dataframes and merges them on the index.'''
    weatherData2=weatherData[["dateCol", "Precip"]]
    mergedData=citiBikeData.merge(weatherData2, how = 'left', left_on="date", right_on="dateCol").set_index(citiBikeData.index)
    del mergedData["dateCol"]
    return mergedData

def generateNetWeatherMatrix():
    '''This function generates a net change matrix with weather data attached, so we 
    can take the weather into consideration when approximating the number of bikes 
    at a station.'''
    df_net = net_matrix_build(df_net, station_data)
    data = weatherDataLoad()
    df_weather = mergeWeatherData(data, df_net)
    df_weather['day of week'] = df_weather.index.map(lambda t: days[t.weekday()])
    df_weather['hour'] = df_weather.index.map(lambda t: t.hour)
    df_weather['month'] = df_weather.index.map(lambda t: t.month)
    aggregation=df_weather[df_weather["Precip"] != 1].groupby(["day of week", "hour", "month"]).mean()
    aggregation=np.round(aggregation, 0)
    del aggregation["Precip"]
    aggregation.to_csv("AggregatedDF.csv")