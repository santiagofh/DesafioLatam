import sys
usuarios_normales = int(sys.argv[1])
usuarios_premium = int(sys.argv[2])
usuarios_prueba = int(sys.argv[3])
presio_venta = int(sys.argv[4])
gastos = int(sys.argv[5])
utilidades=(presio_venta*usuarios_normales)+(presio_venta*usuarios_premium*2)+(usuarios_prueba)-gastos
print("usuarios normales: " + str(usuarios_normales))
print("usuarios premium: " + str(usuarios_premium))
print("usuarios prueba: " + str(usuarios_prueba))
print("presio suscripción: " + str(presio_venta))
print("gastos: "+str(gastos))
print("Las utilidades son: "+str(utilidades))