# %% 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as dt
import numpy as np
import os

import geopandas as gpd


# %% [markdown]

https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda
pip install descartes


# %% [markdown]

# Santiago:
'http://www.ide.cl/index.php/planificacion-y-catastro/item/1948-microdatos-censo-2017-manzana'

# Census data and shape file

stgo_census_data = 'data\Microdatos_Censo_2017%3A_Manzana.csv'
stgo_data = pd.read_csv(stgo_census_data)

stgo_data.groupby('REGION')['TOTAL_PERSONAS'].sum()
# %%

stgo_census_shape_zipfile = 'data/Microdatos_Censo_2017%3A_Manzana-shp.zip'
stgo_census_shape_zipfile = 'Users/Tom/geo_exploration/data/Microdatos_Censo_2017%3A_Manzana-shp.zip!Manzana_2017_2.shp'

stgo_shp = gpd.read_file('zip:///'+stgo_census_shape_zipfile)

# %%



# %%
list = gpd.datasets
# %%

# %%
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
nybb = gpd.read_file(gpd.datasets.get_path('nybb'))

# %%

Chile last Census is 2017
NYC las