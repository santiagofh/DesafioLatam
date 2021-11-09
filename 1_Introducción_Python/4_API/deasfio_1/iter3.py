#%%
from iter1 import ventas
def filter_dict(diccionario,parametro):
    dict={k: v for k, v in diccionario.items() if v > parametro}
    return dict
dict_1=filter_dict(ventas,45000)
# %%
