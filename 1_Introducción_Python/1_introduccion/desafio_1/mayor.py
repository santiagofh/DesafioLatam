import sys
ls=[]
if len(sys.argv)==4:
    for i in sys.argv[1:4]:
        ls.append(int(i))
    print("El numero mayor es: "+str(max(ls)))
else:
    print("Cantidad de argumentos debe ser 3")