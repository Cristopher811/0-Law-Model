import numpy as np

TA = float(input("bla: "))
TB = float(input("bla: "))
A = np.full((10,10),TA)
B = np.full((10,10),TB)
EQ = (TA + TB)/2

C = np.concatenate((A, B), axis = 1)
D = C.copy()

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < len(arreglo) and 0 <= p[1] < len(arreglo[0]):
            validos.append(p)
    return validos

def eq(C):
    tolerance = 1e-9
    for i in range(len(C)):
        for j in range(len(C[i])):
            tol_value = EQ - C[i][j]
            tol_value = abs(tol_value)
            if (tol_value > tolerance):
                return 0
    return 1

n=0
while(eq(C) == 0):
    n += 1
    for i in range(len(C)): #Recorre y almacena los vecinos en vecinos
        for j in range(len(C[i])):
            vecinos = conseguir_vecinos(i,j,C)
            suma_de_vecinos = 0
            for p in vecinos: #suma el valor de los vecinos (p[0] y p[1])
                suma_de_vecinos += C[p[0]][p[1]]
            prom_vecinos = (suma_de_vecinos)/len(vecinos)
            D[i][j] = prom_vecinos
    C = D.copy()
    print(C, end='\n\n')
    print(n)
