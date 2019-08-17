import numpy as np
import panda as pd

np.random.seed(101) # Todos os numeros que gerar vão ser iguais em todo computador

df = pd.DataFrame(np.random.randn(5,4), index="A B C D E".split(), columns="W X Y Z".split())

bol = df >0 #vai retornar uma tabela de booleanos
df[bol] # Numeros onde true, NaN onde false
df(df['W']>0) #Nesse caso, vai excluir as linhas onde não atende. Retorna em numeros
df[df['W']>0]['Y'] #Pega a coluna Y, mas só das linhas onde o W é maior que zero
df[(df['W']>0) & (df['Y']>1)] # 'and' só compara booleanos, tem que ser o &

df.reset_index() #Adiciona uma coluna de números ao lado de A, B, C...
df.set_index('W') #W vai virar o índice

