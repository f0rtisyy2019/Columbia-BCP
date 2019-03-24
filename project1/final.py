import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from math import sin, cos, sqrt, atan2, radians

def convert_latlon(slat, slon, elat, elon):
    R = 6373.0
    dlon = elon - slon
    dlat = elat - slat
    a = sin(dlat / 2)**2 + cos(slat) * cos(elat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance_km = R * c
    distance_m = distance_km * 0.621371
    return distance_m

mta = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"/Resources/mta_station.csv")
df = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"/Resources/final_house_data.csv")
df = df.reset_index().drop(['index', 'Unnamed: 0'], axis=1)
mta = mta.reset_index().drop(['index', 'Unnamed: 0'], axis=1)
df = df[df['distance_miles']<0.1]

station_count = []
for _,home in df.iterrows():
    H_lat = radians(home['latitude'])
    H_lon = radians(home['longitude'])
    print(H_lat, H_lon)
    distance = []
    for _,station in mta.iterrows():
        E_lat = radians(station['GTFS Latitude'])
        E_lon = radians(station['GTFS Longitude'])
        tmp = convert_latlon(H_lat, H_lon, E_lat, E_lon)
        distance.append(tmp)
    print(distance)
    # station_count.append(len(distance[distance < 0.3]))

        
# df['Station number'] = station_count


