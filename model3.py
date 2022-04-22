import numpy as np

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < len(arreglo) and 0 <= p[1] < len(arreglo[0]):
            validos.append(p)
    return validos

N = int(input("Ingrese el tamaño de la matriz NxN: "))

c = 0
Z1 = np.zeros((1, N+2))
Z2 = np.zeros((1,1))
Z3 = np.zeros((N+1, N+2))

A = np.full((N,N), 25)
M1 = np.full((N, 1), 1)
M4 = np.full((N, 1), 4)
A = np.append(M1, A, axis = 1)
A = np.append(A, M4, axis = 1)
A = np.append(A, Z1, axis = 0)
A = np.append(Z1, A, axis = 0)

M2 = np.full((1, N), 2)
M2 = np.append(M2, Z2, axis = 1)
M2 = np.append(Z2, M2, axis = 1)
M2 = np.append(M2, Z3, axis = 0)

M3 = np.full((1, N), 3)
M3 = np.append(M3, Z2, axis = 1)
M3 = np.append(Z2, M3, axis = 1)
M3 = np.append(Z3, M3, axis = 0)

S = A + M2 + M3
S_copia = S.copy()

print(S_copia)

for x in range (0, 100):
  temp2 = x
  temp3

while(c <= 1):
  for i in range (N+2):
    for j in range (N+2):
      if(i == 0 or j == 0):
        S_copia[i][j] = S[i][j]
      elif(i == N+1 or j == N+1):
        S_copia[i][j] = S[i][j]
      else:
        vecinos = conseguir_vecinos(i, j, S)
        sum_vecinos = 0
        for p in vecinos: 
          sum_vecinos += S[p[0]][p[1]]
          prom_vecinos = (sum_vecinos)/len(vecinos)
          S_copia[i][j] = prom_vecinos
      S = S_copia.copy()
      print(S_copia)
      c += 1
