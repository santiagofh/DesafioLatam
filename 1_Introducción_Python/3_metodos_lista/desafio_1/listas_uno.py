#%%
from velocidad import promedio
#%%
auto1 = ['Mazda RX4', 21.0, 6, False, 4] 
auto2 = ['Merc 240D', 24.4, 4, True, 2] 
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3] 
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]
autos=[auto1,auto2,auto3,auto4,auto5,auto6]


# %% 1
def lista_uno(autos):
    autos1=[auto[0] for auto in autos]
    return autos1
lista_uno(autos)
# %% 3

promedio_vel=promedio([(auto[1]) for auto in autos])
[print(i[0]) for i in autos if (i[1]) >= promedio_vel]
# %% 4
[print(auto[0]) for auto in autos if auto[3]==True]
# %% 5

promedio_vel=promedio([(auto[1]) for auto in autos])
mayor_que_promedio=[]
# %%
