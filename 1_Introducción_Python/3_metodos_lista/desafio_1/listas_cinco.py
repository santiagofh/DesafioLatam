# %% 5
import pandas as pd
from pandas.core import indexing
from velocidad import promedio
auto1 = ['Mazda RX4', 21.0, 6, False, 4] 
auto2 = ['Merc 240D', 24.4, 4, True, 2] 
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3] 
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]
autos=[auto1,auto2,auto3,auto4,auto5,auto6]
cars=pd.read_csv("cars.csv",index_col="Unnamed: 0")
mtcars_preproc=pd.read_csv("mtcars_preproc.csv",index_col="Unnamed: 0")

promedio_mpg=promedio([(auto[1]) for auto in autos])
def mayor_promedio(valor):
    if valor >=promedio_mpg:
        return True
    else:
        return False
def lista_mpg(autos):
    autos1=[auto[1] for auto in autos]
    return autos1

filter_mpg = list(filter(mayor_promedio, lista_mpg(autos)))
print(str(list(filter_mpg)))
# %%