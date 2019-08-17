import numpy as np
import pandas as pd

#As vezes você trabalha com banco de dados e encontra dados faltantes
d = {'A':[1, 2, np.nan], 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]}
df = pd.DataFrame(d)
df.dropna() #Exclui as linhas com valores nan
df.dropna(tresh=2) #Exclui as llinhas com dois valores faltantes
df.fillna(value='A') #Substitui pelo valor passado

df.fillna(method='ffill') #Substitui pelos ultimos valores

