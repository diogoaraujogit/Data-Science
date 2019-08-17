import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import pandas as pd

data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['Texto1','Texto2','Texto3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Título da barra de cores'})

layout = dict(geo = {'scope':'usa'})
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)

#Dados reais
df = pd.read_csv('2011_US_AGRI_Exports')
df.head()

data = dict(type='choropleth',
            colorscale = 'YIOrRd',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Milhões de dólares"}
            )

layout = dict(title = '2011 Exportações de Agricultura dos EUA por Estado',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)

#Mapa-mundi Choropleth
df = pd.read_csv('2014_World_GDP')
df.head()

data = dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'GDP Billions US'},
      )

layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = {'type':'Mercator'}
    )
)

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)

