import numpy as np
import pandas as pd

#O método groupby permite agrupar linhas de dados em conjunto e chamar funções agregadas
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Venda':[200,120,340,124,243,350]}
df = pd.DataFrame(data)

group = df.groupby('Empresa')
group.sum() #Soma o numero de vendas por empresa O python entende que é só para numeros. Pode usar varias operações mean, etc..
group.describe() #Retorna várias operações
group.count() # Conta vários tipos de dados
