import numpy as np
import pandas as pd

df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')

#Matplotlib tem folhas de estilo que você pode usar para tornar seus plots mais agradáveis
df1['A'].hist()
import matplotlib.pyplot as plt
plt.style.use('ggplot')
df1['A'].hist()

plt.style.use('bmh')
df1['A'].hist()

plt.style.use('dark_background')
df1['A'].hist()

plt.style.use('fivethirtyeight')
df1['A'].hist()

plt.style.use('ggplot')

#Tipos de plotagem
df2.plot.area(alpha=0.4)

df2.plot.bar()

df2.plot.bar(stacked=True)

df1['A'].plot.hist(bins=50)

df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)

df1.plot.scatter(x='A',y='B')

df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')

df1.plot.scatter(x='A',y='B',s=df1['C']*200)

df2.plot.box()

df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')

#KDE
df2['a'].plot.kde()
df2.plot.density()
