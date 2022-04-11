# %% 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as dt
import numpy as np

import geopandas as gpd


# %% [markdown]


pip install descartes



# %%
A = np.random.random(10)

# %%
list = gpd.datasets
# %%


chile = gpd.read_file('Microdatos_Censo_2017%3A_Manzana-shp.zip')
# %%
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
nybb = gpd.read_file(gpd.datasets.get_path('nybb'))

# %%

Chile last Census is 2017
NYC las