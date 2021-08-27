# -*- coding: utf-8 -*-
"""EU500_FDM_transiente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fu5d9jEZ7GYdFtrdVG-dBYUCIE-hn-6G
"""

# Modelo SIRD
import numpy as np
import matplotlib.pyplot as plt
import math

beta1 = 1;    # (novos infectados/infectados)/dt
beta2 = 0.08
gama = 0.05; # (recuperados/infectados)/dt
mi = 5e-4    # taxa de mortalidade
dt = 1       # 1 dia

m = 365; # periodos de simulação

# Cria vetores para armazenamento dos dados:
S1 = np.empty(m);
I1 = np.empty(m);
R1 = np.empty(m);
D1 = np.empty(m);
t1 = np.empty(m);

S2 = np.empty(m);
I2 = np.empty(m);
R2 = np.empty(m);
D2 = np.empty(m);
t2 = np.empty(m);

# Condições iniciais:
N = 209e6; # População brasileira
S1[0] = N;
I1[0] = 5; # Nùmero inicial de infectados
R1[0] = 0; # Curados 
D1[0] = 0; # Mortos
t1[0] = 0; # tempo

S2[0] = N;
I2[0] = 5; # Nùmero inicial de infectados
R2[0] = 0; # Curados 
D2[0] = 0; # Mortos
t2[0] = 0; # tempo

#beta1:
for i in range(m-1):
  t1[i+1] = t1[i] + dt
  S1[i+1] = S1[i]*(1 - (beta1*I1[i]/N)*dt)
  I1[i+1] = I1[i]*(1 - dt*gama + (beta1*S1[i]/N)*dt - dt*mi)
  R1[i+1] = R1[i] + gama*I1[i]*dt
  D1[i+1] = D1[i] + mi*I1[i]*dt

#beta2:
for i in range(m-1):
  t2[i+1] = t2[i] + dt
  S2[i+1] = S2[i]*(1 - (beta2*I2[i]/N)*dt)
  I2[i+1] = I2[i]*(1 - dt*gama + (beta2*S2[i]/N)*dt - dt*mi)
  R2[i+1] = R2[i] + gama*I2[i]*dt
  D2[i+1] = D2[i] + mi*I2[i]*dt

texto1 = 'D1 = ' + str(math.floor(D1[m-1]))
texto2 = 'D2 = ' + str(math.floor(D2[m-1]))

plt.figure(figsize=(9, 5))
plt.subplot(1,2,1)
plt.plot(t1,S1,label='S')
plt.plot(t1,I1,label='I')
plt.plot(t1,R1,label='R')
plt.plot(t1,D1,label='D')
plt.annotate(texto1, (270,10000000))
plt.xlabel('tempo [dia]')
plt.ylabel('num. pessoas')
plt.legend()
plt.title('Beta = 1')
plt.subplot(1,2,2)
plt.plot(t2,S2,label='S')
plt.plot(t2,I2,label='I')
plt.plot(t2,R2,label='R')
plt.plot(t2,D2,label='D')
plt.annotate(texto2, (290,10000000))
plt.xlabel('tempo [dia]')
plt.ylabel('num. pessoas')
plt.legend()
plt.title('Beta = 0.08')

plt.tight_layout()
plt.savefig('Gráficos_FDM_transinte.pdf')