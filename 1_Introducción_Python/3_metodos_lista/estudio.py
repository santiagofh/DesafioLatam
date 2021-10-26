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
