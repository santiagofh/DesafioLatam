#%%
import string
var=int(input("ingrese un numero: "))
def gen(var):
    print(string.ascii_lowercase[:var])
gen(var)
#%%
def letra_i(n):
    for i in range(0,n):
        if (i == 0) | (i == n-1):
            print("*"*n)
        else:
            print(" "*int(n/2)+"*"+" "*int(n/2))
letra_i(var)
#%%
def letra_o(n):
    for i in range(0,n):
        if (i == 0) | (i == n-1):
            print("*"*n)
        else:
            print("*"+" "*(n-2)+"*")
letra_o(var)
#%%
def letra_x(n):
    for i in range(0,n):
        if i < int(n/2):
            print(" "*int(i)+"*"+" "*int(n-i-i)+"*")
        elif i == int(n/2):
            print(" "*int(n/2+1)+"*")
        else:
            print(" "*int(n-i-1)+"*"+" "*int(i-(n-i-2))+"*")
letra_x(var)
# %%
