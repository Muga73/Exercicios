import numpy as np
from numpy import pi, sin, cos, arccos
from numpy.linalg import norm

def CrossProductMatrix(v):
  return np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])

def RotationMatrix(vetor, angulo):
  K = CrossProductMatrix(vetor)
  return np.eye(3) + sin(angulo)*K + (1-cos(angulo))*K.dot(K)

def RotMat2Vector(vetor1, vetor2):
  theta = arccos(vetor1.dot(vetor2)/(norm(vetor1)*norm(vetor2)))
  vetor = np.cross(vetor1,vetor2)
  if norm(vetor)==0:
    return np.eye(3)
  vetor = vetor/norm(vetor)
  return RotationMatrix(vetor, theta)

def RotMat2Point(p1,p2):
  # Considerando que o elemento foi definido no eixo X, v1 = [1,0,0]
  # Inserir os pontos das extremidades do elemento na forma de arrays (vetores) com 3 elementos 
  return RotMat2Vector(np.array([1,0,0]),p2-p1)

# Exemplo:

# Coordenadas do primeiro nó do elemento:
p1 = np.array([1,1,0])

# Coordenadas do segundo nó do elemento:
p2 = np.array([2,3,0])

# Calcula e exibe a matriz de rotação espacial (3x3):
print(RotMat2Point(p1,p2))

# Para usar essa matriz de rotação com elemento de barra ou viga espacial, deve-se expandi-la 
# para contemplar os graus de liberdade de ambos os nós (ver exemplo da matriz de rotação 2D na aula 09) 