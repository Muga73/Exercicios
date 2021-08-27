
"""

@author: Biella
"""

import numpy as np;
from numpy import pi, cos, sin, sqrt, arctan2;


def Klocal(E,A,L):
    return np.array([[E*A/L,0,0,-E*A/L,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [-E*A/L,0,0,E*A/L,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0]])

# Área da barra (todas):
A = 491e-6;

# Módulo de elasticidade:
E = 205e9;

# Matriz de rigidez do sistema (ref. global)(Nós x 3 g.L):
Ksis = np.zeros((60,60));

#Dimensões das barras (1.25metros e 0.625metros)
L1=L2=L3=L4=L5=L6=L7=L8=L9=L12=L13=L16=L17=L18=L19=L20=L21=L22=L23=L24=L25=L26=L27=L28=L29=L30=L31=L32=L33=L34=L35=L36=L37=L38=L39=L40=L41=L42=L43=L44=L45=L46=L47=L48 = 1.25
L10=L11=L14=L15 = 0.625

#Klocal das barras
K10=K11=K14=K15= Klocal(E,A,L10)
K1=K2=K3=K4=K5=K6=K7=K8=K9=K12=K13=K16=K17=K18=K19=K20=K21=K22=K23=K24=K25=K26=K27=K28=K29=K30=K31=K32=K33=K34=K35=K36=K37=K38=K39=K40=K41=K42=K43=K44=K45=K46=K47=K48 = Klocal(E,A,L1)

#Rlocal das barras
Rsistema1= np.array([[1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1]]);

Rsistema3= np.array([[0.4016, 0, -0.9157, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0],
                      [0.9157, 0, 0.4016, 0, 0, 0],
                      [0, 0, 0, 0.4016, 0, -0.9157],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0.9157, 0, 0.4016]])

Rsistema4= np.array([[-0.5496, 0, -0.8354, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0.8354, 0, -0.5496, 0, 0, 0],
             [0, 0, 0, -0.5496, 0, -0.8354],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0.8354, 0, -0.5496]])

Rsistema5= np.array([[0.5299, -0.8479, 0, 0, 0, 0],
            [0.8479, 0.5299, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0.5299, -0.8479, 0],
            [0, 0, 0, 0.8479, 0.5299, 0],
            [0, 0, 0, 0, 0, 1]])
 
Rsistema6= np.array([[0.2122, -0.8489, -0.4839, 0, 0, 0],
                     [0.8489, 0.4054, -0.3389, 0, 0, 0],
                     [0.4839, -0.3389, 0.8068, 0, 0, 0],
                     [0, 0, 0, 0.2122, -0.8489, -0.4839],
                     [0, 0, 0, 0.8489, 0.4054, -0.3389],
                     [0, 0, 0, 0.4839, -0.3389, 0.8068]])

Rsistema2= np.array([[1.1102e-16, -1.00e+00, 0.00e+00, 0, 0, 0],
                     [1.000e+00, 1.1102e-16, 0.00e+00, 0, 0, 0],
                     [0.00e+00, 0.00e+00, 1.000e+00, 0, 0, 0],
                     [0, 0, 0, 1.1102e-16, -1.00e+00, 0.00e+00],
                     [0, 0, 0, 1.000e+00, 1.1102e-16, 0.00e+00],
                     [0, 0, 0, .00e+00, 0.00e+00, 1.000e+00]])


R1=R2=R3=R4=R5=R6=R7=R8=R9=R10=R11=R12=R13=R14=R15=R16= Rsistema1 #barras no eixo x
R17=R18=R19=R20=R21=R22=R23=R24=R25=R26=Rsistema2 #barras com inclinação de 60° paralelas ao eixo x 
R27=R29=R31=R33=R35=R37=R39=R41= Rsistema3  #barras com inclinação de 300° paralelas ao eixo z
R28=R30=R32=R34=R36=R38=R40=R42= Rsistema4  #barras com inclinação de 60° paralelas ao eixo y
R45=R46=R47=R48= Rsistema5 #barras com inclinação de 60° paralelas ao eixo z
R43=R44= Rsistema6 #barras com inclinação de 60° nas vistas laterias

#Barra 1 (nós 1 e 2)

K1global = R1.dot(K1.dot(np.transpose(R1)));

#Barra 2 (nós 2 e 3)

K2global = R2.dot(K2.dot(np.transpose(R2)));

#Barra 3 (nós 3 e 4)

K3global = R3.dot(K1.dot(np.transpose(R3)));

#Barra 4 (nós 4 e 5)

K4global = R4.dot(K1.dot(np.transpose(R4)));

#Barra 5 (nós 6 e 7)

K5global = R5.dot(K1.dot(np.transpose(R5)));

#Barra 6 (nós 7 e 8)

K6global = R6.dot(K1.dot(np.transpose(R6)));

#Barra 7 (nós 8 e 9)

K1global = R7.dot(K1.dot(np.transpose(R7)));

#Barra 8 (nós 9 e 10)

K8global = R8.dot(K1.dot(np.transpose(R8)));

#Barra 9 (nós 11 e 12)

K1global = R9.dot(K1.dot(np.transpose(R9)));

#Barra 10 (nós 12 e 13)

K10global = R10.dot(K1.dot(np.transpose(R10)));

#Barra 11 (nós 13 e 14)

K11global = R11.dot(K11.dot(np.transpose(R11)));

#Barra 12 (nós 14 e 15)

K12global = R12.dot(K12.dot(np.transpose(R12)));

#Barra 13 (nós 16 e 17)

K13global = R13.dot(K13.dot(np.transpose(R13)));

#Barra 14 (nós 17 e 18)

K14global = R14.dot(K14.dot(np.transpose(R14)));

#Barra 15 (nós 18 e 19)

K15global = R15.dot(K15.dot(np.transpose(R15)));

#Barra 16 (nós 19 e 20)

K16global = R16.dot(K16.dot(np.transpose(R16)));

#Barra 17 (nós 1 e 6)

K17global = R17.dot(K17.dot(np.transpose(R17)));

#Barra 18 (nós 2 e 7)

K18global = R18.dot(K18.dot(np.transpose(R18)));

#Barra 19 (nós 3 e 8)

K19global = R19.dot(K19.dot(np.transpose(R19)));

#Barra 20 (nós 4 e 9)

K20global = R20.dot(K20.dot(np.transpose(R20)));

#Barra 21 (nós 5 e 10)

K21global = R21.dot(K21.dot(np.transpose(R21)));

#Barra 22 (nós 11 e 16)

K22global = R22.dot(K22.dot(np.transpose(R22)));

#Barra 23 (nós 12 e 17)

K23global = R23.dot(K23.dot(np.transpose(R23)));

#Barra 24 (nós 13 e 18)

K24global = R24.dot(K24.dot(np.transpose(R24)));

#Barra 25 (nós 14 e 19)

K25global = R25.dot(K25.dot(np.transpose(R25)));

#Barra 26 (nós 15 e 20)

K26global = R26.dot(K26.dot(np.transpose(R26)));

#Barra 27 (nós 1 e 11)

K27global = R27.dot(K27.dot(np.transpose(R27)));

#Barra 28 (nós 2 e 11)

K28global = R28.dot(K28.dot(np.transpose(R28)));

#Barra 29 (nós 2 e 12)

K29global = R29.dot(K29.dot(np.transpose(R29)));

#Barra 30 (nós 3 e 12)

K30global = R30.dot(K30.dot(np.transpose(R30)));

#Barra 31 (nós 3 e 14)

K31global = R31.dot(K31.dot(np.transpose(R31)));

#Barra 32 (nós 4 e 14)

K32global = R32.dot(K32.dot(np.transpose(R32)));

#Barra 33 (nós 4 e 15)

K33global = R33.dot(K33.dot(np.transpose(R33)));

#Barra 34 (nós 5 e 15)

K34global = R34.dot(K34.dot(np.transpose(R34)));

#Barra 35 (nós 6 e 16)

K35global = R35.dot(K35.dot(np.transpose(R35)));

#Barra 36 (nós 7 e 16)

K36global = R36.dot(K36.dot(np.transpose(R36)));

#Barra 37 (nós 7 e 17)

K37global = R37.dot(K37.dot(np.transpose(R37)));

#Barra 38 (nós 8 e 17)

K38global = R38.dot(K38.dot(np.transpose(R38)));

#Barra 39 (nós 8 e 19)

K39global = R39.dot(K39.dot(np.transpose(R39)));

#Barra 40 (nós 9 e 19)

K40global = R40.dot(K40.dot(np.transpose(R40)));

#Barra 41 (nós 9 e 20)

K41global = R41.dot(K41.dot(np.transpose(R41)));

#Barra 42 (nós 10 e 20)

K42global = R42.dot(K42.dot(np.transpose(R42)));

#Barra 43 (nós 1 e 16)

K43global = R43.dot(K43.dot(np.transpose(R43)));

#Barra 44 (nós 5 e 20)

K44global = R44.dot(K44.dot(np.transpose(R44)));

#Barra 45 (nós 1 e 7)

K45global = R45.dot(K45.dot(np.transpose(R45)));

#Barra 46 (nós 2 e 8)

K46global = R46.dot(K46.dot(np.transpose(R46)));

#Barra 47 (nós 3 e 9)

K47global = R47.dot(K1.dot(np.transpose(R47)));

#Barra 48 (nós 4 e 10)

K48global = R48.dot(K1.dot(np.transpose(R48)));


Fsis_forçaperpendicular = np.array([0,-10000,0]); #AZUL
Fsis_forçaperpendicular = np.array([0,10000, 0]); #AZUL
Fsis_forçacombinada = np.array([0,0,-10000]); #VERMELHA
Fsis_forçacombinada = np.array([-10000,0,0]); #VERMELHA
Fsis_forçavento = np.array([-10000,0,0]);       #ROXA
Fsis_carga= np.array([0,0,-10000]); #VERDE
