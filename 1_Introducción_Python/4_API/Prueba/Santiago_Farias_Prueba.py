#%%
import json
import requests

"""Generate API Key

Your API key for ciencia.visitar-0l@icloud.com is:

Btn6cdCIeEZgzbRjtJ812F1kh0F0fuSZQjQvED6n
You can start using this key to make web service requests. Simply pass your key in the URL when making a web request. Here's an example:

https://api.nasa.gov/planetary/apod?api_key=Btn6cdCIeEZgzbRjtJ812F1kh0F0fuSZQjQvED6n
For additional support, please contact us. When contacting us, please tell us what API you're accessing and provide the following account details so we can quickly find you:

Account Email: ciencia.visitar-0l@icloud.com
Account ID: 6340f522-a8f3-41d7-9e56-bc53209366fb"""

key="UcFlUBnRLMoBHEfvTlUjiJhO7BZSSRsey6gURvgp"

url= "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=UcFlUBnRLMoBHEfvTlUjiJhO7BZSSRsey6gURvgp"

metodo="GET"
requerimiento=requests.request(metodo,url)
print(type(requerimiento))
print(type(requerimiento.json()))
info=requerimiento.json()["photos"]
print(type(info))

#se extraen las primera 25 fotos
fotos=[]
n=0
for i in info:
    if n<25:
        fotos.append(i["img_src"])
        n+=1
print(len(fotos))

def build_web_page(lista):
#contruye un sitio web 
    html=""
    i=0

    x=len(lista)
    html="<html>\n<head>\n<body>\n<url>\n"

    while i < x:
        html +="<li><img src=\"{}\" \"width=\"400\" height=\"400\">\n".format(fotos[i])
        i += 1
    html+="<html>\n<head>\n<body>\n<url>\n"

    with open ("output.html","w") as f:
        f.write(html)
build_web_page(fotos)

# %%
