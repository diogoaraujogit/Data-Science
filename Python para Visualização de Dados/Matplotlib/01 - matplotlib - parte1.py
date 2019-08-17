# Biblioteca de visualização de dados mais popular do python
# semelhante aos métodos de plotagem do matlab
# na documentação tem um bom material

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x*x

#Functional
plt.plot(x, y, 'r') # 'r' é a cor vermelha (red)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Título')
plt.show()

# plt.subplot(nlinhas, ncols, numeroplot)
plt.subplot(1,2,1)  #O utltimo elemento se refere o grafico
plt.plot(x, y, 'r--')
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-')

#orientado a objetos
# Cria uma figura vazia
fig = plt.figure()

# Adiciona eixos à figura
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # esquerda, inferior, largura, altura (faixa de 0 a 1)

# Plota nos eixos especificados
axes.plot(x, y, 'b')
axes.set_xlabel('Define o Label X') # Perceba o uso de "set_" para começar métodos
axes.set_ylabel('Define o Label Y')
axes.set_title('Define o Título')

#Várias outras configurações no jupyter
