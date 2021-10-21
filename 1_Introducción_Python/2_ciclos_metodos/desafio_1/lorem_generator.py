# %%
import sys
import lorem
var=int(sys.argv[1])
print("Lorem de "+str(var)+" parrafos.\n")
for i in range(var):
    p = lorem.paragraph()
    print(p+"\n")
# %%
