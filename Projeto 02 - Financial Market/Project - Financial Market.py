from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime

#Dados
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# Bank of America
BAC = data.DataReader("BAC", 'yahoo', start, end)

# CitiGroup
C = data.DataReader("C", 'yahoo', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'yahoo', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'yahoo', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'yahoo', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'yahoo', start, end)

# Could also do this for a Panel Object
df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],'yahoo', start, end)

#Criando uma lista de símbolo dos tickers
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

#  concatenando os DataFrames do banco juntos em um único chamado bank_stocks
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)

#Definindo os níveis dos nomes das colunas
bank_stocks.columns.names = ['Bank Ticker','Stock Info']


#Análise de dados exploratória

#preço máximo de fechamento para o estoque de cada banco durante todo o período
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

# Este dataframe conterá os retornos para a ação de cada banco
returns = pd.DataFrame()

#Usando o método pct_change () pandas na coluna close para criar uma coluna que represente esse valor de retorno.
for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()

# Crie um parplot utilizando seaborn no dataframe de retorno
#returns[1:]
import seaborn as sns
sns.pairplot(returns[1:])

# descubrindo quais datas cada ação dos bancos teve o melhor e o pior dia de retorno.
returns.idxmin()
returns.idxmax()

#Encontrando a ação mais arriscada com base no desvio padrão
returns.std() # Citigroup é a mais arriscada

#Criando um distplot usando seaborn dos retornos de 2015 para Morgan Stanley
sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)

# Criando um distplot usando seaborn dos retornos de 2008 para CitiGroup
sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)

#mais visualizações
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Criando um gráfico de linha mostrando o preço de fechamento para cada banco para todo o índice de tempo
for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()

#Médias móveis
#  a média de 30 dias para o preço próximo do Bank Of America para o ano de 2008
plt.figure(figsize=(12,6))
BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()

# mapa de calor da correlação entre os preços de fechamento das ações
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

# usando o clustermap do seaborn para agrupar as correlações
sns.clustermap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)

