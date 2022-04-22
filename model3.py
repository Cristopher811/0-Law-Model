import numpy as np

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < len(arreglo) and 0 <= p[1] < len(arreglo[0]):
            validos.append(p)
    return validos

N = int(input("Ingrese el tamaño de la matriz NxN: "))
q = int(100/(N-1))

c = 0
Z1 = np.zeros((1, N+2))

A = np.full((N,N), 25)
M1 = np.full((N, 1), 1)
M4 = np.full((N, 1), 4)
A = np.append(M1, A, axis = 1)
A = np.append(A, M4, axis = 1)
A = np.append(A, Z1, axis = 0)
A = np.append(Z1, A, axis = 0)

print('\n Cuerpo sin modificar', A)

for i in range (N+2):
  for j in range (N+2):
    if((i==0 or i == N+1) and (0<j<N+1)):
      if(j == 1):
        A[i][j] = 0
      else:
        A[i][j] = A[i][j-1] + q

A_copia = A.copy()
print('\n Cuerpo con T3 y T4 variando linealmente', A)
      
while(c <= 1):
  for i in range (N+2):
    for j in range (N+2):
      if(i == 0 or j == 0):
        A_copia[i][j] = A[i][j]
      elif(i == N+1 or j == N+1):
        A_copia[i][j] = A[i][j]
      else:
        vecinos = conseguir_vecinos(i, j, A)
        sum_vecinos = 0
        for p in vecinos: 
          sum_vecinos += A[p[0]][p[1]]
          prom_vecinos = (sum_vecinos)/len(vecinos)
          A_copia[i][j] = prom_vecinos
      A = A_copia.copy()
      print(A_copia)
      c += 1