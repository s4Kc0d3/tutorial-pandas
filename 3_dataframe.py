# El objeto DataFrame
# Puedes ver un DataFrame como una hoja de cálculo, con valores en celdas
# nombres de columna y etiquetas de índice para cada fila.
# Permite definir expresiones para calcular columnas basadas en otras columnas,
# crear tablas dinámicas, agrupar filas, dibujar gráficos, etc...
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Forma no común de crear DataFrame
data = {
    "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
    "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
    "children": pd.Series([0, 3], index=["charles", "bob"]),
    "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
}

df = pd.DataFrame(data)

# Forma común de crear
df = pd.DataFrame({
    "birthyear": {"alice": 1985, "bob": 1984, "charles": 1992},
    "hobby": {"alice": "Biking", "bob": "Dancing"},
    "weight": {"alice": 68, "bob": 83, "charles": 112},
    "children": {"bob": 3, "charles": 0}
})

# Acceder a los valores de este DataFrame
print("\nAccedemos al vcalor weight: df['weight']")
print(df["weight"])

# Acceder a varios valores del DataFrame
print("\nAccedemos a dos valores: df[['weight','birthyear']]")
print(df[["weight", "birthyear"]])

# indexamos con la etiqueta
print("\nIndexamos con la etiqueta: df.loc['alice']")
print(df.loc["alice"])

# indexamos con la posición
print("\nIndexamos con la posición: df.iloc[0]")
print(df.iloc[0])

# Crear y eliminar nuevas columnas con un DataFrame existente
print("\nCrear columna nueva a un DataFrame existente. creamos 'height'")
df["height"] = pd.Series({"alice": 167, "bob": 180})
print(df)

print("\nEliminamos la columna creada 'height'")
del df['height']
print(df)

print("\nAñadir columna en una posición específica. por ejemplo posición 2.")
df.insert(2, "height", pd.Series({"alice": 167, "bob": 180}))
print(df)

print("\nCrear nuevas columnas a partir de otras de manera sencilla.")
df["w2h_ratio"] = df["weight"] / df["height"]
print(df)

# Operaciones: Son como en las Series
new_df = df[["weight", "height"]]
print("\nCreo nuevo DF a partir del existente con dos columnas")
print(new_df)
print("\nSumamos 2 a los valores en todas las columnas")
new_df = new_df+2
print(new_df)
print("\nTambién podemos pasar DataFrames a funciones de numpy")
print(np.exp(new_df))

# Filtrado
# Podemos usar el indexado de tipo masking para filtrar los valores de un DataFrame
print("\nFiltramos los weight > 80")
print(df[df["weight"] > 80])

# Filtrando por varias columnas
print("\nFiltramos los weight > 80 y los height >= 180")
print(df[(df['weight'] > 80) & (df['height'] >= 180)])

# Visualización
# También podemos utilizar la función plot() sobre un DataFrame para visualizar los datos de manera rápida.
# Esto es especialmente útil cuando todos los datos que tenemos son de tipo numérico.
new_df.plot()
plt.show()
