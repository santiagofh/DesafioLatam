#%%
import sys
ventas={
    'Enero':15000,
    'Febrero':22000,
    'Marzo':12000,
    'Abril':17000,
    'Mayo':81000,
    'Junio':13000,
    'Julio':13000,
    'Agosto':41200,
    'Septiembre':25000,
    'Octubre':21500,
    'Noviembre':91000,
    'Diciembre':21000
}
list=(sys.argv[1:])
for i in list:
    for mes, venta in ventas.items():
        if int(i) == venta:
            print(mes)
            
        else:
            print("no encontrado")
            
# %%
