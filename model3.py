import numpy as np

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < len(arreglo) and 0 <= p[1] < len(arreglo[0]):
            validos.append(p)
    return validos

'''
def equivalentes(C, T1, T2):
    tolerance = 1e-9
    EQ = (T1 + T2)/2
    for i in range(len(C)):
        for j in range(len(C[i])):
            tol_value = EQ - C[i][j]
            tol_value = abs(tol_value)
            if (tol_value > tolerance):
                return 0
    return 1
'''

N = int(input("Ingresa la dimensión N de la matriz NxN: "))
TA = float(input("Ingresa la temperatura del cuerpo A: "))
TM1 = float(input("Ingresa la primer temperatura externa: "))
TM2 = float(input("Ingresa la segunda temperatura externa:" ))
TM3 = float(input("Ingresa la tercera temperatura externa: "))
TM4 = float(input("Ingresa la cuarta temperatura extrena: "))

c = 0
Z1 = np.zeros((1, N+2))
Z2 = np.zeros((1,1))
Z3 = np.zeros((N+1, N+2))

A = np.full((N,N),TA)
M1 = np.full((N, 1), TM1)
M4 = np.full((N, 1), TM4)
A = np.append(M1, A, axis = 1)
A = np.append(A, M4, axis = 1)
A = np.append(A, Z1, axis = 0)
A = np.append(Z1, A, axis = 0)


M2 = np.full((1, N), TM2)
M2 = np.append(M2, Z2, axis = 1)
M2 = np.append(Z2, M2, axis = 1)
M2 = np.append(M2, Z3, axis = 0)

M3 = np.full((1, N), TM3)
M3 = np.append(M3, Z2, axis = 1)
M3 = np.append(Z2, M3, axis = 1)
M3 = np.append(Z3, M3, axis = 0)

S = A + M2 + M3
S_C = S.copy()



print('\n\n Cuerpo M1:\n\n ', S)

while(c <= 2):
  for i in range (N+1):
    for j in range (N+1):
      if((i == N+1 or i == 0) or (j == N+1 or j == 0)):
        S_C[i][j] = S[i][j]
      else:
        vecinos = conseguir_vecinos(i, j, S)
        sum_vecinos = 0
        for p in vecinos: 
          sum_vecinos += S[p[0]][p[1]]
          prom_vecinos = (sum_vecinos)/len(vecinos)
          S_C[i][j] = prom_vecinos
      S = S_C.copy()
      c += 1
      print(S_C)
    