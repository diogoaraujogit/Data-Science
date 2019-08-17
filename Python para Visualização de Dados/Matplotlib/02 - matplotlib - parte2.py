import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x*x
# Uso semelhante a plt.figure (), exceto usar o desempacotamento da tupla para agarrar as figuras e os eixos
fig, axes = plt.subplots()

# Agora usando o objeto dos eixos para adicionar coisas ao gráfico
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Título')

#Tela vazia de 1 por 2 subplots
fig, axes = plt.subplots(nrows=1, ncols=2)

#Podemos iterar através dessa matriz
for ax in axes:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')

# Ajustando o tamanho da figura
fig, axes = plt.subplots(figsize=(12,3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('título');

#Salvando figuras (podendo escolher até o dpi)
fig.savefig("filename.png", dpi=200)

#Legendas
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()

#Mais opções no Jupyter]
