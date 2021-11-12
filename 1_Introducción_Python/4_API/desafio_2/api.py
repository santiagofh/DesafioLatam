
#%%
import json
import requests

url = "https://reqres.in/api/users"
metodo= "GET"
response= requests.request("GET",url)
user_data=json.loads(response.text)
#%% 1
print(user_data)
#%% 2 created_user
payload={
    "name": "ignacio",
    "job": "profesor"
}
response=requests.request("POST",url,data=payload)
created_user=(response.text)
print(created_user)
# %% update users
payload={
    "name": "morpheus",
    "job": "zion"
}
response=requests.request("PUT",url,data=payload)
update_user=(response.text)
print(update_user)
# %%
payload={
    "name": "pepe"
}
response=requests.request("DELETE",url,data=payload)
print(response)
# %%
