# %%
velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25] 
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]
print(len(velocidad))
print(len(distancia))
lista_vel_dist=list(zip(velocidad,distancia))
from velocidad import promedio
promedio_velocidad = promedio(velocidad)
promedio_distancia = promedio(distancia)
# %% Velocidad bajo el promedio
cont=0
for i in velocidad:
    if i <=promedio_velocidad:
        cont+=1
print("Velocidad bajo el promedio: "+str(cont))
# %% Velocidad bajo el promedio y distancia sobre el promedio
cont=0
for i in lista_vel_dist:
    if (i[0] <= promedio_velocidad) | (i[1] > promedio_distancia):
        cont+=1
print("Velocidad bajo el promedio y distancia sobre el promedio: "+str(cont))
# %% Velocidad sobre el promedio
cont=0
for i in velocidad:
    if i >promedio_velocidad:
        cont+=1
print("Velocidad sobre el promedio: "+str(cont))
# %% Velocidad sobre el promedio y distancia bajo el promedio
cont=0
for i in lista_vel_dist:
    if (i[0] > promedio_velocidad) | (i[1] < promedio_distancia):
        cont+=1
print("Velocidad sobre el promedio y distancia bajo el promedio: "+str(cont))
# %% 
