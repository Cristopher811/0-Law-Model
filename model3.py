import numpy as np

size = (3,6)

A = np.array([
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
])
B = np.array([
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20]
])


C = np.concatenate((A, B), axis = 1)
print(C)
D = C.copy()

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < size[0] and 0 <= p[1] < size[1]: 
            validos.append(p)
    return validos

for i in range(len(C)): #Recorre y almacena los vecinos en vecinos
    for j in range(len(C[i])):
        vecinos = conseguir_vecinos(i,j,C)
        print(vecinos, end='\n\n')
        suma_de_vecinos = 0
        for p in vecinos: #suma el valor de los vecinos (p[0] y p[1])
            suma_de_vecinos += C[p[0]][p[1]]
        print(suma_de_vecinos)
        prom_vecinos = (suma_de_vecinos)/len(vecinos)
        D[i][j] = prom_vecinos
        print(prom_vecinos)

print(D)


