#%%
ventas={
    'Enero':15000,
    'Febrero':22000,
    'Marzo':12000,
    'Abril':17000,
    'Mayo':81000,
    'Junio':13000,
    'Julio':21000,
    'Agosto':41200,
    'Septiembre':25000,
    'Octubre':21500,
    'Noviembre':91000,
    'Diciembre':21000
}
def filter_dict(diccionario,parametro):
    dict={k: v for k, v in diccionario.items() if v > parametro}
    return dict
#%% EJEMPLO
dict_1=filter_dict(ventas,45000)
print("ejemplo: dict_1=filter_dict(ventas,45000)")
print(dict_1)
# %%
