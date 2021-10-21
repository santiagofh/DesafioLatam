import sys
g = float(sys.argv[1])
r = int(sys.argv[2])*1000
respuesta=(2*r*g)**0.5
print("Gravedad (m/s^2)): " + str(g))
print("Radio (m): " + str(r))
print("La velocidad de escape es: "+str(respuesta)+" m/s^2")