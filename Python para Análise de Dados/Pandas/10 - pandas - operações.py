import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

df['col2'].unique() #Retorna a coluna apenas com valores exclusivos
df['col2'].nunique() #Quantidade de valores unicos
df['col2'].value_counts() #A quantidade cada valor

# Selecione do DataFrame usando critérios de várias colunas
newdf = df[(df['col1']>2) & (df['col2']==444)]

#Também pode aplicar funções. Funciona como o map
def times2(x):
    return x*2
df['col1'].apply(times2)

df['col3'].apply(len) #Tamanho dos dados da coluna
df['col1'].sum() # Soma os dados da coluna
del df['col1'] # Remove as colunas permanentemente

df.sort_values(by='col2') #Ordenando a coluna . inplace=False por padrão
df.isnull() # Retorna uma tabela de booleanos mostrando quem é null(true)
