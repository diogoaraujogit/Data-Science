# Pandas é uma biblioteca de código fonte aberto escrita sobre o numpy
# È raápida, muito semelhante ao excel.
# trabalha com dados de diferentes tipos

import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
arr = np.array([10, 20, 30])
minha_lista = [10, 20, 30]
d = {'a':10, 'b':20, 'c':30}

pd.Series(data=minha_lista, index=labels) #Gera uma series. Muito parecido com dicionários

ser1 = pd.Series([1, 2, 3], index=['EUA', 'Germany', 'France'])
ser2 = pd.Series([1, 2, 3], index=['EUA', 'Brazil', 'France'])
ser1 + ser2 # Soma os numeros de cada país, Germany e Brazil ficam com NaN

