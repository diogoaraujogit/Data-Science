import numpy as np
import pandas as pd

#Niveis de indice
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside)) #Criar uma lista de tuplas através do zip
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=['A', 'B']) #Vai criar multiniveis
df.loc['G1'].loc[1] # Uma forma de acessar os dados
df.index.names = ['Grupo', 'Numero'] #Dando nomes aos indices
df.xs(1, level='Numero') #Parecido co o loc, mas pode puxar de níveis internos