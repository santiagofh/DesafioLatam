def funcion_perdidas(dataframe,var,print_lis=False):
    import pandas as pd
    lista=list(dataframe[var])
    var_perdidas=[x for x in lista if str(x)=='nan']
    cantidad=len(var_perdidas)
    porcentaje=len(var_perdidas)/len(lista)
    if print_lis:
        na=dataframe.loc[dataframe[var].isna()==True]
        print(na[['ccodealp','ht_region']])
    return cantidad,porcentaje
    

def funcion_grafico_2(dataframe,plot_by,plot_var,statistic='mean',global_stat=False):
    import matplotlib.pyplot as plt
    if statistic == 'mean':
        groupby_mean_df=dataframe.groupby(plot_by)[plot_var].mean()
        plt.plot(groupby_mean_df.values,groupby_mean_df.index,'o')
        if global_stat:
            plt.axvline(dataframe[plot_var].mean(),color='tomato',linestyle='--',)
    if statistic == 'median':
        groupby_median_df=dataframe.groupby(plot_by)[plot_var].median()
        plt.plot(groupby_median_df.values,groupby_median_df.index,'o')
        if global_stat:
            plt.axvline(dataframe[plot_var].mean(),color='tomato',linestyle='--',)
