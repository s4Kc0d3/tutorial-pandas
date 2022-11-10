import pandas as pd

# Creando objeto series
s = pd.Series([1, 2, 3])

# Para meterle etiquetas
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Como acceder a los valores del objeto "indexado"
# Primera opción como etiqueta
print("Acceder por etiqueta, opción NO RECOMENDADA.")
print(s['a'], s['b'], s['c'])

# Como posición en la secuencia
print("Acceder por indice, opción NO RECOMENDADA")
print(s[0], s[1], s[2])

# acceder por etiqueta, LA MANERA BUENA
print("Acceder por etiqueta, opción RECOMENDADA s.loc['etiqueta']")
print(s.loc['a'])

# acceder por índice, LA MANERA BUENA
print("Acceder por indice, opción RECOMENDADA s.iloc[indice]")
print(s.iloc[2])

# crear objeto Series como un dict tradicional de python
print("Creando objeto series como dict tradicional de python")
data = {"a": 1, "b": 2, "c": 3}
s = pd.Series(data)
print(s)

# Operaciones matemáticas
print("Sumar un 2 a la serie: s = s + 2")
s = s + 2
print(s)
print("Multiplicar: s = s * 2")
s = s * 2
print(s)
print("Dividir, etc...")

# Escoger los dos últimos elementos
print("Escoger los dos últimos elementos: s[-2:]")
print(s[-2:])

# filtrado
print("Filtrado, por ejemplo de mi serie dame los valores igual o mayor a 2: s[s>=2] ")
print(s[s>=2])

# Operaciones entre dos mismos tipos de objetos
s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
s3 = pd.Series({'a': 1, 'b': 2, 'd': 3})
print("Sumar dos series: s2 + s3")  # Sumará los que coincidan con la misma etiqueta
print(s2 + s3)