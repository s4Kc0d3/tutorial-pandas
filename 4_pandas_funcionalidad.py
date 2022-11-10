# Antes construiamos los DataFrames a partir de Diccionarios
# Ahora se aprenderá a partir de ficheros grandes de datos.

import pandas as pd
import numpy as np
import wget
import os
import zipfile

# La forma básica de construir DataFrames
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# descargar datos
url = 'https://mymldatasets.s3.eu-de.cloud-object-storage.appdomain.cloud/ml-1m.zip'

if not os.path.exists('ml-1m.zip'):
    wget.download(url)

    # extraer datos
    with zipfile.ZipFile('ml-1m.zip', 'r') as zip_ref:
        zip_ref.extractall()

# listamos directorio
print("")
print(os.listdir('ml-1m'))

# cargo la información
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)

# visualizamos los primeros elementos
print(users.head())

# en caso que los archivos sean json, se pueden leer con df.read_json o si fuera csv con df.read_csv
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames)
print(ratings.head())

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames, encoding='unicode_escape')
print(movies.head())

# de la misma manera podemos exportarlo en csv
movies.to_csv('movies.csv', index=False)

# si cargamos ahora el csv generado podemos ver que tenemos exactamente los mismos datos
_movies = pd.read_csv('movies.csv')
print(_movies.head())

# la segunda funcionalidad es la de mezclar varios DataFrames en uno solo.
# para ello se utiliza "merge"
# primero mezclamos el objeto ratings y users. Para ellos Pandas utiliza la columna en común users_id
# para saber que filas corresponden al mismo usuario en cada objeto. Después, hacemos lo mismo
# con el objeto movies. En este caso, Pandas utiliza la columna movies_id para relacionar las filas de los
# dos DataFrames.
# Pandas ofrece otras funciones para mezclar Dataframes como join o concat, cada una de ellas mezclando
# los datos de una manera determinada.
# Puedes ver mas info en: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
data = pd.merge(pd.merge(ratings, users), movies)
print(data.head())

# Información básica
# número de filas y columnas
print("Número de filas y columnas: data.shape")
print(data.shape)

# nombres de las columnas
print("nombres de las columnas")
print(data.columns)

# información general
print("información general")
print(data.info())

print("información general con estadística")
print(data.describe())

# Agrupar Datos
# Si te fijas en el dataset tenemos muchas entradas repetidas, tanto para usuarios como para películas
# (un usuario puede opinar sobre varias películas, y una película puede tener opiniones de varios usuarios).
# Para agrupar todos los datos según una columnas en concreto, podemos una la funcion groupby.
data_title = data.groupby('title')
print(data_title.size())

# Una función muy potente en Pandas es la función pivot_table, que nos permite agrupar los datos de un DataFrame
# según los valores de alguna columna. Por ejemplo, si queremos conocer la puntuación media de cada película
# en nuestro dataset separada por género, podemos conseguirlo de la siguiente manera.
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings.sample(5))

# FILTRAR DATOS
# Y si ahora quisiésemos quedarnos solo con aquellas entradas en el DataFrame generado que tengan como mínimo
# 250 opiniones?
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 150]
print(active_titles)

# Ahora, podemos usar estos índices para indexar en el DataFrame que nos interesa.
mean_ratings_250 = mean_ratings.loc[active_titles]
print(mean_ratings_250.sample(5))

# ORDENAR DATOS
# Ordenar por genero Femenino
top_female_ratings = mean_ratings_250.sort_values(by='F', ascending=False)
print(top_female_ratings.head())

# Y si nos interesa conocer aquellas películas con mayor discrepancia entre hombres y mujeres?
mean_ratings_250['diff'] = np.abs(mean_ratings_250['M'] - mean_ratings_250['F'])
sorted_by_diff = mean_ratings_250.sort_values(by='diff', ascending=False)
print(sorted_by_diff.head())

# TRATAR DATOS AUSENTES
# en ocasiones podemos encontrar que en nuestro DataFrame hay valores ausentes, lo que se conoce
# como missing data o missing values. Puede ser porque no existen en la fuente de la informacion
# extraida, o bien en una operación llevada a cabo en los datos.
df = pd.DataFrame({
    "weight": {"alice":68, "charles": 112},
    "height": {"bob": 168, "charles": 182}
})
print(df)

# podemos conocer cuantos valores ausentes hay con la funcion isna.
print(df.isna())

# valores ausentes por columnas
print(df.isna().sum())

# valores ausentes por filas
print(df.isna().sum(axis=1))

# En el ejemplo anterior tenemos un DataFrame con varios valores ausentes.
# La primera opción que nos da Pandas para tratar estos valores es simplemente reemplazarlos
# por otro con la función "fillna".

# reemplazar NaN por 0
print(df.fillna(0))

# reemplazar NaN por el valor medio de la columna
print(df.fillna(df.mean()))

# elimina todas las filas con algún valor NaN
print(df.dropna())

# elimina todas las filas con todos los valores en NaN
print(df.dropna(how='all'))

# elimina todas las columnas con todos los valores en NaN
print(df.dropna(axis=1, how='all'))