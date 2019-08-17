import seaborn as sns

flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')

#Heatmap
sns.heatmap(tips.corr())
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)

flights.pivot_table(values='passengers',index='month',columns='year')
pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)

#O clustermap usa agrupamento hierárquico para produzir uma versão em cluster do heatmap.
sns.clustermap(pvflights, standard_scale=1)
# Mais opções para obter a informação um pouco mais clara, como a normalização
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)