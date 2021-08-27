# Carrega bibliotecas:
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos;
import numpy.linalg as la;

dx = 2.5e-3;

# Matriz dos coeficientes das incognitas:
MatrizA = np.array([[-2, 1, 0, 0],
					[ 1,-2, 1, 0],
					[ 0, 1,-2, 1],
					[ 0, 0,-1, 1]]);

# Vetor dos termos independentes:
VetorB = np.array([-dx**2-300, -dx**2, -dx**2, 7e3*dx])

# Solucao do sistema linear
phi = la.solve(MatrizA, VetorB)

print(phi)
