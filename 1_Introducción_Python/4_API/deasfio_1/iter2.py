#%%
from iter1 import ventas
for mes, venta in ventas.items():
    if venta >= 45000:
        print(mes)
# %%
