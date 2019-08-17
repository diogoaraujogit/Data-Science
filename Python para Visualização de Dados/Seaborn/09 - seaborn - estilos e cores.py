import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

#Pode definir um tipo específico
sns.countplot(x='sex',data=tips)

sns.set_style('white')
sns.countplot(x='sex',data=tips)

sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')

#Remoção dos limites
sns.countplot(x='sex',data=tips)
sns.despine()

sns.countplot(x='sex',data=tips)
sns.despine(left=True)

#controlar a proporção de tamanho e aspecto da maioria dos plots do seaborn passando parâmetros: size e aspect.
# Plot não gradeado
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)

# Plot tipo grade
sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips)

#Escala e Contexto
#O set_context () permite que você substitua parâmetros padrão:
sns.set_context('poster',font_scale=4)
sns.countplot(x='sex',data=tips,palette='coolwarm')

