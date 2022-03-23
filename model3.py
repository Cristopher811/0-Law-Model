import numpy as np

n_1 = 0
n_2 = 0
n_3 = 0
N = int(input("Ingresa la dimensión N de la matriz NxN: "))
TA = float(input("Ingresa la temperatura del cuerpo A: "))
TB = float(input("Ingresa la temperatura del cuerpo B: "))
TC = float(input("Ingresa la temperatura del cuerpo C: "))

A = np.full((N,N),TA)
B = np.full((N,N),TB)
C = np.full((N,N),TC)

AB = np.concatenate((A, B), axis = 1)
AB_copia = AB.copy()

BC = np.concatenate((B,C), axis = 1)
BC_copia = BC.copy()

AC = np.concatenate((A,C), axis = 1)
AC_copia = AC.copy()

print('\n\n Cuerpo AB:')
print(AB, end='\n\n Cuerpo BC: \n')
print(BC, end='\n\n Cuerpo AC: \n')
print(AC, end='\n\n')

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < len(arreglo) and 0 <= p[1] < len(arreglo[0]):
            validos.append(p)
    return validos

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

while(equivalentes(AB, TA, TB) == 0):
    n_1 += 1
    for i in range(len(AB)): #Recorre y almacena los vecinos en vecinos
        for j in range(len(AB[i])):
            vecinos = conseguir_vecinos(i,j,AB)
            suma_de_vecinos = 0
            for p in vecinos: #suma el valor de los vecinos (p[0] y p[1])
             suma_de_vecinos += AB[p[0]][p[1]]
            prom_vecinos = (suma_de_vecinos)/len(vecinos)
            AB_copia[i][j] = prom_vecinos
    AB = AB_copia.copy()

while(equivalentes(BC, TB, TC) == 0):
    n_2 += 1
    for i in range(len(BC)): #Recorre y almacena los vecinos en vecinos
        for j in range(len(BC[i])):
            vecinos = conseguir_vecinos(i,j,BC)
            suma_de_vecinos = 0
            for p in vecinos: #suma el valor de los vecinos (p[0] y p[1])
             suma_de_vecinos += BC[p[0]][p[1]]
            prom_vecinos = (suma_de_vecinos)/len(vecinos)
            BC_copia[i][j] = prom_vecinos
    BC = BC_copia.copy()

while(equivalentes(AC, TA, TC) == 0):
    n_3 += 1
    for i in range(len(AC)): #Recorre y almacena los vecinos en vecinos
        for j in range(len(AC[i])):
            vecinos = conseguir_vecinos(i,j,AC)
            suma_de_vecinos = 0
            for p in vecinos: #suma el valor de los vecinos (p[0] y p[1])
             suma_de_vecinos += AC[p[0]][p[1]]
            prom_vecinos = (suma_de_vecinos)/len(vecinos)
            AC_copia[i][j] = prom_vecinos
    AC = AC_copia.copy()

print('\n\n Cuerpo AB:')
print(AB, end='\n\n El equilibrio térmico entre A y B se alcanzó después de ')
print(n_1, end=' iteraciones. \n\n Cuerpo BC: \n')
print(BC, end='\n\n El equilibrio térmico entre B y C se alcanzó después de ')
print(n_2, end=' iteraciones. \n\n Cuerpo AC: \n')
print(AC, end='\n\n El equilibrio térmico entre A y C se alcanzó después de ')
print(n_3, end=' iteraciones. \n\n')