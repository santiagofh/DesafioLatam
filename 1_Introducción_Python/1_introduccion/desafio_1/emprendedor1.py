import sys
presio_venta = int(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])
utilidades=presio_venta*usuarios-gastos
print("Presio de venta: " + str(presio_venta))
print("Usuarios: " + str(usuarios))
print("Gastos: "+str(gastos))
print("Las utilidades son: "+str(utilidades))