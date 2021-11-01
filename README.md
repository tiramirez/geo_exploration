# Geo_exploration

Personal repo to play with geographic data.
Any input, correction, or idea is welcome.


## Index

| Name | Description | Status | Date |
|-|-|-|-|
|Boston.ipynb| Learn to work with US Census Data | WIP | 2021-10-29 |
|osm | Learn to use OSM library | Not started |  |
|pltal| Automatic calcualation of accessibility to Public Transit | Not started | | 

## Census Data
* https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-data.html


## Set Environment
Follow the code bellow
```
conda create -p ./env
conda activate ./env
conda install --channel conda-forge geopandas
conda install -c conda-forge --prefix ./env ipykernel -y
```
Optional (I have not tried it)
```
conda install pygeos --channel conda-forge
```


## Errors when not using `conda-forge`

* oserror could not find lib c or load any of its variants
```
conda uninestall Shapely
conda inestall Shapely
```

* Error: Kernel is dead ([link](https://stackoverflow.com/questions/49326164/jupyter-notebook-dead-kernel))
```
conda install -c conda-forge jupyterlab
conda install -c anaconda ipython
```

* Error with GDAL ([link](https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda))