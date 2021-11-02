#%%
import pandas as pd
df=pd.read_csv("athlete_events.csv")
df_chile=df.loc[df.Team=="Chile"]
df_chile.Year.value_counts()
df_chile_ganadores=df_chile.loc[df_chile.Medal.isnull()==False]
df_chile_ganadores.Name.value_counts()
df_chile_ganadores.Year.value_counts()
# %%
