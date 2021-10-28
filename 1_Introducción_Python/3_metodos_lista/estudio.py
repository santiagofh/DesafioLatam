#%%
paises = ['Chile', 'Perú', 'Argentina']
paises.insert(1, 'Bolivia')

# %%
animales = ['gato', 'perro', 'hurón', 'pez', 'nogal', 'conejo']
animales.remove('nogal')
animales = ['gato', 'perro', 'hurón', 'pez', 'nogal', 'conejo','tapir']

# %%
'tapir' in animales
# %%
letras=['a','b','c']
for i in letras:
    print(letras[i])
# %%
from functools import reduce
animals=['gato','perro','hurón']
reduce(lambda x,y : x+y,animals)
# %%
import numpy as np
primera = np.arange(50)
segunda = primera[10:20]
segunda[2] = "100"
print(primera[12])
# %%
mascotas = np.array(["Copi-Copi", "Elemento", "Adjetivo",
"Mente en Blanco", "Chaucha", "Cabecita", "Bigote", "Mutante"])
especies = np.array(["perro", "perro", "perro", "perro", "perro", "gato", "gato","gato"])
filtrados = mascotas[~(especies == 'gato')]
# %%
