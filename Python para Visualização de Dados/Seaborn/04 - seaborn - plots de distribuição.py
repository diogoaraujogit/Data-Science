#Bilbioteca de visualização estatística de dados
#Excelentes padrões de estilo
#Funciona em harmonia com os dataframes do pandas

import seaborn as sns

#Seaborn vem com conjuntos de dados embutidos.
tips = sns.load_dataset('tips')

#O distplot mostra a distribuição de um conjunto de observações de uma variável.
sns.distplot(tips['total_bill'])

#Para remover a camada kde e apenas usar o histograma:
sns.distplot(tips['total_bill'],kde=False,bins=30)

#jointplot() permite combinar basicamente dois distplots() para dados bivariados. Podemos visualizar os dados das seguintes formas (usando o kind):
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')

#pairplot irá traçar distribuições entre pares em todo o DataFrame (para as colunas numéricas) e suporta um argumento de matiz de cor (para colunas categóricas).
sns.pairplot(tips)

#rugplots possuem um conceito muito simples, eles apenas desenham uma marca de traço para cada ponto em uma distribuição univariada. Eles são o bloco de construção de um KDE:
sns.rugplot(tips['total_bill'])


