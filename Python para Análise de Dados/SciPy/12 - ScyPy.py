import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,8]])

#Álgebra linear
from scipy import linalg

# Determinante de uma matriz
linalg.det(A)

#a decomposição de LU girada de uma matriz
P, L, U = linalg.lu(A)
np.dot(L,U)

#Autovetores e Autovalores
EW, EV = linalg.eig(A)

#Solução de sistemas de equações
v = np.array([[2],[3],[5]])
s = linalg.solve(A,v)

#Álgebra Linear Esparsa

from scipy import sparse

A = sparse.lil_matrix((1000, 1000))
A[0,:100] = np.random.rand(100)
A[1,100:200] = A[0,:100]
A.setdiag(np.random.rand(1000))

#Algebra linear com matrizes esparsas
from scipy.sparse import linalg

# Converte esta matriz para o formato linha esparsa comprimida.
A.tocsr()
A = A.tocsr()
b = np.random.rand(1000)
linalg.spsolve(A, b)
