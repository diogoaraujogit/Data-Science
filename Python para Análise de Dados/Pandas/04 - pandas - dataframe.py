#DataFrama conjunto se Series
import numpy as np
import pandas as pd

np.random.seed(101) # Todos os numeros que gerar vão ser iguais em todo computador

df = pd.DataFrame(np.random.randn(5,4), index="A B C D E".split(), columns="W X Y Z".split())
# Vai ser uma tabela. Index vai ser o nome das linhas, os random vão ser os dados. É uma planilha de excel

df['W'] #Extrai a coluna W. df.W também funciona

df['new'] = df['W'] + df['X'] #Pode criar desse jeito
df.drop('new', axis=1) # Para deletar colunas. Mas não muda o df, o new continua lá
df = df.drop('new', axis=1) #Agora sim deleta o new
df.drop('new', axis=1, inplace=True) #Assim tbm deleta

df.loc['A', 'W'] # Passa linhaxcoluna para encontrar o valor. Também usa para seleção de vários valores
df.iloc[1:4, 2:] #iloca usa números de referência