import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

#Pairgrid é um plot de grade para traçar relacionamentos entre pares de um conjunto de dados.
# Just the Grid
sns.PairGrid(iris)

# Then you map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)

# Altera os tipos de plots na diagonal, parte superior e inferior.
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

# Pairplot é uma versão mais simples do PairGrid (você usará com bastante frequência)
sns.pairplot(iris)
sns.pairplot(iris,hue='species',palette='rainbow')

#FacetGrid é a maneira geral de criar plots de grades com base em um recurso:
tips = sns.load_dataset('tips')

# Só a grade
g = sns.FacetGrid(tips, col="time", row="smoker")

g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")

g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Observe como os argumentos vêm após a chamada do plt.scatter
g = g.map(plt.scatter, "total_bill", "tip").add_legend()

# JointGrid é a versão geral para grades tipo jointplot (), para um exemplo rápido:
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.distplot)



