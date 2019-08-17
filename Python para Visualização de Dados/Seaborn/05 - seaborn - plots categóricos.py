import seaborn as sns

tips = sns.load_dataset('tips')

#** barplot ** é um gráfico geral que permite que você agregue os dados categóricos baseados em alguma função, por padrão, a média:
sns.barplot(x='sex',y='total_bill',data=tips)

#Você pode alterar o objeto estimador para sua própria função, que converte um vetor em um escalar:
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

#countplot é essencialmente o mesmo que o gráfico de barras, exceto que o estimador está explicitamente contando o número de ocorrências. É por isso que apenas passamos o valor x
sns.countplot(x='sex',data=tips)

#Boxplots e violinplots são usados para mostrar a distribuição de dados categóricos.
sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')

# Podemos orientar os dados para aparecerem na horizontal
sns.boxplot(data=tips,palette='rainbow',orient='h')

sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')

#stripplot e swarmplot
sns.stripplot(x="day", y="total_bill", data=tips)
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)

#Combinando plots categóricos
sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)