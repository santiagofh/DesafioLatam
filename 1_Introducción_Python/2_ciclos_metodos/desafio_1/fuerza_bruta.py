# %%
import string
i=0
while i == 0:
    contraseña=input('ingresa contraseña (solo caracteres validos):\n')
    contraseña=contraseña.lower()
    error=0
    for j in range(len(contraseña)):
        if contraseña[j] not in string.ascii_lowercase:
            error+=1
    if error > 0:
        print('contraseña tiene caracteres incorrectos, intentelo nuevamente\n')
        i=0   
    else:
        i+=1
#%%
cont=1
i=0
while i < len(contraseña):
    l=contraseña[i]
    print('letra a buscar: '+l)
    for j in string.ascii_lowercase:
        if j==l:
            print('intento numero '+str(cont)+': ¿'+l+'=='+j+'? SI')
            i+=1
            cont+=1
            break
        else:
            print('intento numero '+str(cont)+': ¿'+l+'=='+j+'? NO')
            cont+=1
print('el total de intentos fue: '+str(cont-1))
# %%