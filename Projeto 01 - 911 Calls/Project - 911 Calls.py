import numpy as np
import pandas as pd

# Importação das bibliotecas de visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns

#Importação do arquivo como DataFrame
df = pd.read_csv("911.csv")

# Testes
#df.info()
#print(df.head(3))
#print(df['zip'].value_counts().head(5))
#print(df['twp'].value_counts().head(5))
#print(df['title'].nunique())

# Criando novos recursos
# Na coluna "title" existem "Razões / Departamentos" especificados antes do código do título. Iremos separá-las
# em duas colunas distintas
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
df['Reason'].value_counts()

#Usando seaborn  para criar um countplot de chamadas 911 baseadas nesta nova coluna
sns.countplot(x='Reason',data=df,palette='viridis')

#Usando as informções de tempo como datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
#Testes
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
#Transformando os dias da semana de numero para nome
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

#Usando Seaborn para criar um countplot da coluna "Day of Week" com a tonalidade baseada na coluna Reason.
sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# O mesmo para mês
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# criando um objeto groupby chamado "byMonth",
byMonth = df.groupby('Month').count()
# criando um plot simples fora do Dataframe indicando a contagem de chamadas por mês.
# Could be any column
byMonth['twp'].plot()

#Modleo linear do número de chamadas por mês
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

# Criando uma nova coluna chamada 'Data' que contenha a data da coluna timeStamp
df['Date']=df['timeStamp'].apply(lambda t: t.date())

# agrupando esta coluna Data com o groupby. Usando o count () para criar um gráfico de contagens de chamadas 911.
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()

#Criando mapas de calor com Seaborn

#Reestruturando as informações de tempo
dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()

#Criando o HM
plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')

#Clustermap
sns.clustermap(dayHour,cmap='viridis')

# Repetindo e mostrando o mês como coluna
dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')

sns.clustermap(dayMonth,cmap='viridis')





