# import transitfeed
# %%
# import osmnx as ox
import pandas as pd
# import numpy as np
# import geopandas as gpd
# from shapely.geometry import Point
import matplotlib.pyplot as plt

# importing required modules
from zipfile import ZipFile

## Down load data from MBTA
url = "https://cdn.mbta.com/MBTA_GTFS.zip"
r = requests.get(url, allow_redirects=True)
open('./MBTA_GTFS.zip', 'wb').write(r.content)


file_name = "MBTA_GTFS.zip"
gtfs = dict()
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    
    for info in zip.infolist():
        gtfs[info[:-4]]=pd.read_csv(info.filename)
        print(info.filename)
# %%
G = ox.graph_from_place('Manhattan, New York, USA', network_type='drive')
# fig, ax = ox.plot_graph(G)

# A = transitfeed.loader.Loader(zip='gtfs-stgo.zip')

# %%

# https://datos.gob.cl/dataset/gtfs_valdivia

folder = 'valdivia1mar16/'
stops = pd.read_csv(folder+'stops.txt')

# %%

def find_coordinates(df):
    return (
        df
        .assign(
            lat = df.filter(like='lat').astype(float)
          , lng = df.filter(like='lon').astype(float)
        )
    )

def trans_coordinates(df):
    return (
        df
        .assign(
            coordinates = pd.Series(zip(df.lng, df.lat)).apply(Point)
        )
    )
def create_gpd():
    df = pd.read_csv(folder+'stops.txt')
    df = find_coordinates(df)
    df = trans_coordinates(df)
    return gpd.GeoDataFrame(df, geometry='coordinates')



# score[0],score[1] = score['id'].str.split(',',1).str
# score['lat'] = score[0]
# score['long'] = score[1]
# score = score.astype({'lat':float,
#                       'long':float})

# ## Crear una columna nueva
# score['Coordinates'] = list(zip(score.long, score.lat))
# ## Convertir la columna en shape type Points
# score['Coordinates'] = score['Coordinates'].apply(Point)

# score = gpd.GeoDataFrame(score.copy(), geometry='Coordinates')
# %%
