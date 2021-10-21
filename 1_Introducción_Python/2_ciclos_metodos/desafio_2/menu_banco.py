#%% Librerias
import sys
#%% Funciones
mensaje="""Bienvenido al portal del Banco Amigo. Escoja una opción:
1. Consultar saldo
2. Hacer depósito
3. Realizar giro
4. Salir"""
def depositar(saldo, cantidad):
    total=saldo+cantidad
    return total
def girar(saldo, cantidad):
    total=saldo-cantidad
    return total
def mostrar_menu(saldo=0):
    i=0
    while i <= 1:
        print(mensaje)
        opcion=int(input("\nElija una opción: "))
        if opcion == 1:
            print("\n"+"Su saldo es: "+str(saldo)+"\n")
        elif opcion == 2:
            deposito=int(input("\nIngrese la cantidad a depositar: "))
            saldo=depositar(saldo, deposito)
            print("\n"+"Su nuevo saldo es: "+str(saldo)+"\n")
        elif opcion == 3:
            if saldo > 0:
                giro=int(input("\nIngrese la cantidad a girar: "))
                if giro <= saldo:
                    saldo=girar(saldo, giro)
                    print("\n"+"Su nuevo saldo es: "+str(saldo)+"\n")
                else: 
                    print("\n"+"No se puede girar esa cantidad. Su saldo es de: "+str(saldo)+"\n")
        elif opcion == 4:
            print("\n Adios \n")
            i=10
        else:
            print("\nOpción inválida. Por favor ingrese 1, 2, 3 ó 4.\n")
#%% Programa
if len(sys.argv)>1:
    saldo=int(sys.argv[1])
else:
    saldo=0
mostrar_menu(saldo)
# %%
