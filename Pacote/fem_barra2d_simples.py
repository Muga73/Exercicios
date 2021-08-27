import numpy as np;
from numpy import pi, cos, sin, sqrt, arctan2;

def Klocal(E,A,L):
    return np.array([[ E*A/L, 0,-E*A/L, 0],
                     [     0, 0,     0, 0],
                     [-E*A/L, 0, E*A/L, 0],
                     [     0, 0,     0, 0]]);

def RotMat(alfa):
    return np.array([[cos(alfa),-sin(alfa), 0, 0],
                     [sin(alfa), cos(alfa), 0, 0],
                     [0, 0, cos(alfa),-sin(alfa)],
                     [0, 0, sin(alfa), cos(alfa)]]);

# Área da barra (todas):
A = 100e-6;

# Módulo de elasticidade:
E = 210e9;

# Matriz de rigidez do sistema (ref. global):
Ksis = np.zeros((6,6));

# Cálculo da barra 1:
L1 = sqrt(1**2 + 0.7**2);
alfa1 = arctan2(-0.7,1);

K1local = Klocal(E,A,L1);
R1 = RotMat(alfa1);

K1global = R1.dot(K1local.dot(np.transpose(R1)));

# Montagem do K1global na matriz do sistema:
Ksis[2:4,2:4] += K1global[0:2,0:2]; # K22_barra1
Ksis[2:4,4:6] += K1global[0:2,2:4]; # K23_barra1
Ksis[4:6,2:4] += K1global[2:4,0:2]; # K32_barra1
Ksis[4:6,4:6] += K1global[2:4,2:4]; # K33_barra1

# Cálculo da barra 2:
L2 = 0.7;
alfa2 = pi/2;

K2local = Klocal(E,A,L2);
R2 = RotMat(alfa2);

K2global = R2.dot(K2local.dot(np.transpose(R2)));

# Montagem do K2global na matriz do sistema:
Ksis[0:2,0:2] += K2global[0:2,0:2]; # K11_barra2
Ksis[0:2,2:4] += K2global[0:2,2:4]; # K12_barra2
Ksis[2:4,0:2] += K2global[2:4,0:2]; # K21_barra2
Ksis[2:4,2:4] += K2global[2:4,2:4]; # K22_barra2

# Cálculo da barra 3:
L3 = 1;
alfa3 = 0;

K3local = Klocal(E,A,L3);
R3 = RotMat(alfa3);

K3global = R3.dot(K3local.dot(np.transpose(R3)));

# Montagem do K3global na matriz do sistema:
Ksis[0:2,0:2] += K3global[0:2,0:2]; # K11_barra3
Ksis[0:2,4:6] += K3global[0:2,2:4]; # K13_barra3
Ksis[4:6,0:2] += K3global[2:4,0:2]; # K31_barra3
Ksis[4:6,4:6] += K3global[2:4,2:4]; # K33_barra3

# Redução da matriz para determinar somente deslocamento desconhecidos
Ksis_red = np.delete(Ksis, [0,1,2], 0); # exclui as 3 primeiras linhas
Ksis_red = np.delete(Ksis_red, [0,1,2], 1); # exclui as 3 primeiras colunas

# Vetor de forças reduzido
Fsis_red = np.array([0,0,-200]);

x = np.linalg.solve(Ksis_red, Fsis_red);

print("Deslocamentos (y2, x3, y3):\n",x)

# Cálculo das forças:
f = Ksis[0:3,3:6].dot(x);

print("Forças (F1x, F1y, F2x):\n",f);




