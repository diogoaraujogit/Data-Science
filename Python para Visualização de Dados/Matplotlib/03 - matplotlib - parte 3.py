import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x*x

# Cor e estilo da linha como MATLAB
fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-') # linha azul tracejada
ax.plot(x, x**3, 'g--') # linha verde pontilhada

fig, ax = plt.subplots()

ax.plot(x, x+1, color="blue", alpha=0.5) # meio-transparente
ax.plot(x, x+2, color="#8B008B")        # RGB
ax.plot(x, x+3, color="#FF8C00")        # RGB

fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# Possiveis estilos de linha: ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# Traços estilizados
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # Formato: comprimento da linha, comprimento do espaço, ...

# possíveis símbolos de marcador: marcador = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# tamanho e cor do marcador
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");

#Intervalos de distância
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("intervalos de eixos padrão")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("eixos apertados")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("distância personalizada dos eixos");

#Plots especiais
plt.scatter(x,y)

from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# box plot retangular
plt.boxplot(data,vert=True,patch_artist=True);
