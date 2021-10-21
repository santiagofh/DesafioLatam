import sys
parametros=len(sys.argv)
print(parametros)
if parametros <= 4:
    utilidades_anterior=1000
else:
    utilidades_anterior = int(sys.argv[4])
presio_venta = int(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])
utilidades=presio_venta*usuarios-gastos
razon=utilidades/utilidades_anterior
print("presio_venta: " + str(presio_venta))
print("usuarios: " + str(usuarios))
print("gastos: " + str(gastos))
print("utilidades: " + str(utilidades))
print("utilidades periodo anterior: " + str(utilidades_anterior))
print("razon de utilidades: "+str(razon))