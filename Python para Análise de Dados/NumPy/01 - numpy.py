import numpy as np # NumPy (ou Numpy) é uma biblioteca de álgebra linear para Python. É tão importante para a
# Data Science com Python pois quase todas as bibliotecas dependem do NumPy como um dos seus principais blocos de construção.

minha_lista = [1, 2, 3]
np.array(minha_lista) # Vai converter em um array, um vetor

minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(minha_matriz) # Converte em um vetor de 2 dimensões? Pq não 3? Pq uma matriz tem 2 dimensões

np.arange(0, 10, 2) #Cria um vetor com esse intervalor e step

np.zeros(3) #Cria um vetor com 3 zeros
np.zeros((5,5)) #Cria uma matriz 5x5 de zeros
np.ones((2,2))
np.eye(4) #Matriz identidade 4x4 (só a diagonal com 1, resto 0)

np.linspace(0,10,3) # Vai imprimir 0, 5 e 10
np.random.rand(5) # 5 numeros aleatorios de 0 a 1. Se quiser outro range, multiplica
np.random.rand(5,5) #Matriz aleatória de 5x5. randn = distribuição normal

np.random.randInt(0, 100, 10) #Número inteiros. Esse 10 é a quantidade.

arr = np.random.rand(25)
arr.reshape(5,5) # 5 tuplas de 5 elementos. O reshape muda a forma. Deixou de ser um vetor e virou matriz
arr.reshape #Atributo, não tem parentesis. Retorna a forma

arr.max() # E arr.min(), nem precisa enviar nada, já retorna o valor

arr.argmax() # retorna o índice onde o maior elemento se encontra








