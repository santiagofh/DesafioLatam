{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa6d5a6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def funcion_perdidas(dataframe,var,print_lis=False):\n",
    "    import pandas as pd\n",
    "    lista=list(df[var])\n",
    "    var_perdidas=[x for x in lista if str(x)=='nan']\n",
    "    cantidad=len(var_perdidas)\n",
    "    porcentaje=len(var_perdidas)/len(lista)\n",
    "    if print_lis:\n",
    "        na=dataframe.loc[dataframe[var].isna()==True]\n",
    "        print(na[['ccodealp','ht_region']])\n",
    "    return cantidad,porcentaje\n",
    "\n",
    "def funcion_grafico_1(sample_df,full_df,var,sample_mean=False,true_mean=False):\n",
    "    import pandas as pd\n",
    "    import numpy as np\n",
    "    import matplotlib.pyplot as plt \n",
    "    mean_sample=np.mean(sample_df[var])\n",
    "    mean_full=np.mean(full_df[var])\n",
    "    plt.hist(sample_df[var].dropna())\n",
    "    if sample_mean:\n",
    "        plt.axvline(mean_sample, lw=3 , color='green', linestyle='--')\n",
    "    if true_mean:\n",
    "        plt.axvline(mean_full, lw=3 , color='tomato', linestyle='--')\n",
    "    plt.xlabel(var)\n",
    "    plt.ylabel('Frecuencia')\n",
    "    \n",
    "def funcion_grafico_2(dataframe,plot_var,statistic='mean',global_stat=False):\n",
    "    if statistic == 'mean':\n",
    "        groupby_mean_df=dataframe.groupby(plot_by)[plot_var].mean()\n",
    "        plt.plot(groupby_mean_df.values,groupby_mean_df.index,'o')\n",
    "        if global_stat:\n",
    "            plt.axvline(dataframe[plot_var].mean(),color='tomato',linestyle='--',)\n",
    "    if statistic == 'median':\n",
    "        groupby_median_df=dataframe.groupby(plot_by)[plot_var].median()\n",
    "        plt.plot(groupby_median_df.values,groupby_median_df.index,'o')\n",
    "        if global_stat:\n",
    "            plt.axvline(dataframe[plot_var].mean(),color='tomato',linestyle='--',)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.5 64-bit ('base': conda)",
   "language": "python",
   "name": "python395jvsc74a57bd072d69218b7fb2ce1663efa0b5e8f9de2bd757b21f6b239bd8d395fb92f34789b"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
