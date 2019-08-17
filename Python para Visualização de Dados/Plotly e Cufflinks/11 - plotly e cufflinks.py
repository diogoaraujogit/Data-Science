#O Plotly é uma biblioteca que permite criar gráficos interativos que você pode usar em painéis ou sites (você pode salvá-los
# como arquivos html ou imagens estáticas).

import pandas as pd
import numpy as np

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)

import cufflinks as cf

# Para Notebooks
init_notebook_mode(connected=True)
# For offline use
cf.go_offline()

#Dados
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2 = pd.DataFrame({'Categoria':['A','B','C'],'Valores':[32,43,50]})

#Dispersão
df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)

#Plots de barra
df2.iplot(kind='bar',x='Categoria',y='Valores')

#Boxplots
df.iplot(kind='box')

#Superficies 3D
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
df3.iplot(kind='surface',colorscale='rdylbu')

#Spread
df[['A','B']].iplot(kind='spread')

#Histograma
df['A'].iplot(kind='hist',bins=25)

#Bolha
df.iplot(kind='bubble',x='A',y='B',size='C')

#Scatter Matrix
df.scatter_matrix()

