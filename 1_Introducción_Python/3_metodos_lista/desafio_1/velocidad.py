
#%%
def promedio(lista):
    from functools import reduce
    numerador=reduce(lambda x,y:x+y,lista)
    denominador=len(lista)
    promedio=numerador/denominador
    return promedio
# %%
