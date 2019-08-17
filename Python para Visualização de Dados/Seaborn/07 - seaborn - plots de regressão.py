import seaborn as sns

tips = sns.load_dataset('tips')

#** lmplot ** permite que você exiba modelos lineares, mas também permite que você divida esses gráficos com base em recursos
sns.lmplot(x='total_bill',y='tip',data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')

# Trabalhando com marcadores
# http://matplotlib.org/api/markers_api.html
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})

#Usando grades
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm')

#Aspecto e tamanho
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)
