import numpy as np;
from numpy import pi, cos, sin, sqrt, arctan2;

def Klocal(E,A,L,Izz):
    c1 = A * E / L;
    c2 = E * Izz / L ** 3;
    return np.array([[c1, 0, 0, -c1, 0, 0],
                     [0, c2 * 12, c2 * 6 * L, 0, -c2 * 12, c2 * 6 * L],
                     [0, c2 * 6 * L, c2 * 4 * L ** 2, 0, -c2 * 6 * L, c2 * 2 * L ** 2],
                     [-c1, 0, 0, c1, 0, 0],
                     [0, -c2 * 12, -c2 * 6 * L, 0, c2 * 12, -c2 * 6 * L],
                     [0, c2 * 6 * L, c2 * 2 * L ** 2, 0, -c2 * 6 * L, c2 * 4 * L ** 2]]);


def RotMat(alfa):
    return np.array([[cos(alfa), -sin(alfa), 0, 0, 0, 0],
                     [sin(alfa), cos(alfa), 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 0, 0, cos(alfa), -sin(alfa), 0],
                     [0, 0, 0, sin(alfa), cos(alfa), 0],
                     [0, 0, 0, 0, 0, 1]]);


# Área da viga-barra (todas):
A = 100e-6;

# Momento de inércia de área da viga-barra (todas):
Izz = (10e-3)**4/12; # Seção quadrada

# Módulo de elasticidade:
E = 210e9;

# Matriz de rigidez do sistema (ref. global) 3 nós x 3 g.d.l = 9:
Ksis = np.zeros((9,9));

# Cálculo da barra 1:
L1 = sqrt(1**2 + 0.7**2);
alfa1 = arctan2(-0.7,1);

K1local = Klocal(E,A,L1,Izz);
R1 = RotMat(alfa1);

K1global = R1.dot(K1local.dot(np.transpose(R1)));

# Montagem do K1global na matriz do sistema:
Ksis[3:6,3:6] += K1global[0:3,0:3]; # K22_barra1
Ksis[3:6,6:9] += K1global[0:3,3:6]; # K23_barra1
Ksis[6:9,3:6] += K1global[3:6,0:3]; # K32_barra1
Ksis[6:9,6:9] += K1global[3:6,3:6]; # K33_barra1

# Cálculo da barra 2:
L2 = 0.7;
alfa2 = pi/2;

K2local = Klocal(E,A,L2,Izz);
R2 = RotMat(alfa2);

K2global = R2.dot(K2local.dot(np.transpose(R2)));

# Montagem do K2global na matriz do sistema:
Ksis[0:3,0:3] += K2global[0:3,0:3]; # K11_barra2
Ksis[0:3,3:6] += K2global[0:3,3:6]; # K12_barra2
Ksis[3:6,0:3] += K2global[3:6,0:3]; # K21_barra2
Ksis[3:6,3:6] += K2global[3:6,3:6]; # K22_barra2

# Cálculo da barra 3:
L3 = 1;
alfa3 = 0;

K3local = Klocal(E,A,L3,Izz);
R3 = RotMat(alfa3);

K3global = R3.dot(K3local.dot(np.transpose(R3)));

# Montagem do K3global na matriz do sistema:
Ksis[0:3,0:3] += K3global[0:3,0:3]; # K11_barra3
Ksis[0:3,6:9] += K3global[0:3,3:6]; # K13_barra3
Ksis[6:9,0:3] += K3global[3:6,0:3]; # K31_barra3
Ksis[6:9,6:9] += K3global[3:6,3:6]; # K33_barra3

# Redução da matriz para determinar somente deslocamento desconhecidos
Ksis_red = np.delete(Ksis, [0,1,3], 0); # exclui as linhas das forças desconhecidos
Ksis_red = np.delete(Ksis_red, [0,1,3], 1); # exclui as colunas dos deslocamentos conhecidos

# Vetor de forças reduzido
Fsis_red = np.array([0,0,0,0,-200,0]); # M1z, F2y, M2z, F3x, F3y, M3z

x = np.linalg.solve(Ksis_red, Fsis_red);

print("Deslocamentos (theta1, y2, theta2, x3, y3, theta3):\n",x)

# Cálculo das forças:
Ksis_red = np.delete(Ksis, [2,4,5,6,7,8], 0); # exclui as linhas dos deslocamentos desconhecidos
Ksis_red = np.delete(Ksis_red, [0,1,3], 1); # exclui as colunas dos deslocamentos conhecidos
f = Ksis_red.dot(x);

print("Forças (F1x, F1y, F2x):\n",f);

# Elemento de barra:
# Deslocamentos (y2, x3, y3):
# [-6.66666667e-06 -1.36054422e-05 -6.14533875e-05]
# Forças (F1x, F1y, F2x):
# [ 285.71428571  200.         -285.71428571]

# Elemento de viga-barra:
# Deslocamentos (theta1, y2, theta2, x3, y3, theta3):
# [-2.19394835e-05 -6.66568979e-06 -3.31076413e-06 -1.36028656e-05
# -6.14425334e-05 -7.30347313e-05]
# Forças (F1x, F1y, F2x):
# [ 285.71428571  200.         -285.71428571]




