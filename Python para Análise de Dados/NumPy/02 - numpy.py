# Pega elemento normalmente como se faz com listas e etc
# o slice é do mesmo jeito [::]
# para matrizes, usa [::} e [::], ou pode usar [::, ::]

import numpy as np

arr = np.arange(50)
arr2 = arr.copy() #Dessa forma, eu posso alterar o arr2 sem alterar o arr principal

arr >50 #Vai retornar um array de true's or false's

arr + arr #Python permite isso e todas as operações. Por escalar também. Pega item por item.
np.sqrt(arr)
np.exp(arr)
np.mean(arr) # Média
np.std(arr) # Desvio padrão
# np.sin(arr) :: np.max(arr). Na documentação tem todas as funções.

#AltEntrer e ShiftEnter nos exercícios
