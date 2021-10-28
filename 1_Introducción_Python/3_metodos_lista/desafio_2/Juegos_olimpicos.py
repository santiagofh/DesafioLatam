#%%
import pandas as pd
df=pd.read_csv("athlete_events.csv")
#%%
ejercicio_1=df.shape
# %%
competencias=df["Event"].value_counts()
ejercicio_2=len(competencias)
# %%
ejercicio_3=df["Season"].value_counts(normalize=True)
# %%
ejercicio_4=df.loc[(df.Season=="Summer")]
ejercicio_4=ejercicio_4.loc[(ejercicio_4.Year==min(ejercicio_4.Year))]
ejercicio_4=(ejercicio_4["City"].value_counts()).index[0]
# %%
ejercicio_5=df.loc[(df.Season=="Winter")]
ejercicio_5=ejercicio_5.loc[(ejercicio_5.Year==min(ejercicio_5.Year))]
ejercicio_5=(ejercicio_5["City"].value_counts()).index[0]
#%%
ejercicio_6=df['Team'].value_counts()
ejercicio_6=ejercicio_6.head(10)
# %%
ejercicio_7=df["Medal"].value_counts(normalize=True)
# %%
ejercicio_8=df.loc[(df.Season=="Summer")]
ejercicio_8=ejercicio_8.loc[(ejercicio_8.Year==min(ejercicio_8.Year))]
ejercicio_8=ejercicio_8["Team"].unique()
# %%
