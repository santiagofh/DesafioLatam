#%%
import pandas as pd
df=pd.read_csv("athlete_events.csv")
#%%Crear 4 nuevos subsets de datos, donde cada uno contenga, respectivamente, a los atletas que ganaron Oro, Plata, Bronce y aquellos que no ganaron medallas
df_oro=df.loc[df.Medal=='Gold']
df_plata=df.loc[df.Medal=='Bronze']
df_bronce=df.loc[df.Medal=='Silver']
df_nan=df.loc[df.Medal.isnull()==True]
# %%Generar una nueva columna de nombre ​'Female' para cada uno de los subsets creados. En esta nueva columna, se debe asignar ​1 a las filas correspondientes a una mujer, y ​0​ a las correspondientes a un hombre
import numpy as np
def Female(df):
    df['Female']=np.where(df.Sex == 'F',1,0)
Female(df_oro)
Female(df_plata)
Female(df_bronce)
Female(df_nan)
# %%
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
def top_team(df):
    top_team=df.Team.value_counts().head(10)
    name_df=str(namestr(df, globals())).split('\'')[1].split('_')[1]
    print('10 primeros países con mayor cantidad de participantes para el subset: '+(name_df))
    print(top_team)
    print('\n')
    return top_team
top_team_oro=top_team(df_oro)
top_team_plata=top_team(df_plata)
top_team_bronce=top_team(df_bronce)
top_team_nan=top_team(df_nan)
# %%
def report_sex(df):
    sex=df.Sex.value_counts()
    name_df=str(namestr(df, globals())).split('\'')[1].split('_')[1]
    print('Reporte de cantidad de hombres(M) y mujeres(F) para el subset '+(name_df))
    print(sex)
    print('\n')
    return sex

report_sex_oro=report_sex(df_oro)
report_sex_plata=report_sex(df_plata)
report_sex_bronce=report_sex(df_bronce)
report_sex_nan=report_sex(df_nan)
# %%
