#%%
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

def quarter(diccionario):
    diccionario_filtrado={}
    diccionario_filtrado["Q1"]=0
    diccionario_filtrado["Q2"]=0
    diccionario_filtrado["Q3"]=0
    diccionario_filtrado["Q4"]=0
    print(diccionario_filtrado)
    
    for clave,valor in diccionario.items():
        print(clave)
        if clave == ("Enero") or clave ==("Febrero") or clave == ("Marzo"):
            diccionario_filtrado["Q1"] += valor
        elif clave == ("Abril") or clave == ("Mayo") or clave == ("Junio"):
            diccionario_filtrado["Q2"] += valor
        elif clave == ("Julio") or clave == ("Agosto") or clave == ("Septiembre"):
            diccionario_filtrado["Q3"] += valor
        else:
            diccionario_filtrado["Q4"] += valor
  
    return diccionario_filtrado

print(quarter(ventas))
# %%
