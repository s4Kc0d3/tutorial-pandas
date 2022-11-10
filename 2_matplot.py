# Visualización
# Podemos visualizar los datos en una Serie gracias a su integración con Matplotlib
# una libreria de visualización muy útil.
# aquí se puede ver un ejemplo simplemente llamando a la función plot()
# directamente sobre el objeto

import matplotlib.pyplot as plt
import pandas as pd

temperatures = [4.4,5.1,6.1,6.1,6.1,7.5,4.2,9.3,3.5,5.5]
s = pd.Series(temperatures, name="Temperature")
s.plot()
plt.show()