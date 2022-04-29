import numpy as np

def conseguir_vecinos(i,j,  arreglo):
    puntos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    validos = []
    for p in puntos:
        if 0 <= p[0] < len(arreglo) and 0 <= p[1] < len(arreglo[0]):
            validos.append(p)
    return validos
  

N = int(input("Ingrese el tamaño de la matriz NxN: "))
temp = float(input("Ingrese la temperatura del cuerpo contenido: "))

#Constantes utiles
q_const = int(100/(N-1))
eq_total = 0
c_const = 0
Z1 = np.zeros((1, N+2))

#Formacion del cuerpo total
A = np.full((N,N), temp)
M1 = np.full((N, 1), 0)
M4 = np.full((N, 1), 100)
A = np.append(M1, A, axis = 1)
A = np.append(A, M4, axis = 1)
A = np.append(A, Z1, axis = 0)
A = np.append(Z1, A, axis = 0)

#imprimimos el cuerpo antes de generar los valores para T3 y T4
print('\n Cuerpo sin modificar\n', A)
print('\n')

#Algoritmo para generar los valores T3 y T4 de manera lineal de T1 a T2
for i in range (N+2):
  for j in range (N+2):
    if((i==0 or i == N+1) and (0<j<N+1)):
      if(j == 1):
        A[i][j] = 0
      else:
        A[i][j] = A[i][j-1] + q_const

#Generamos una copia de A para hacer las iteraciones
A_copia = A.copy()

  
while(eq_total == 0):
  tolerance = 1e-10
  eq_value = 0
  for i in range (N+2):
    for j in range (N+2):
      #Condicionales para mantener estos valores constantes
      if(i == 0 or j == 0):
        A_copia[i][j] = A[i][j]
      elif(i == N+1 or j == N+1):
        A_copia[i][j] = A[i][j] 
      #Proceso de iteracion de las temperaturas sacando el promedio de las adyacentes
      else:
        vecinos = conseguir_vecinos(i, j, A)
        sum_vecinos = 0
        for p in vecinos: 
          sum_vecinos += A[p[0]][p[1]]
          prom_vecinos =  (sum_vecinos)/len(vecinos)
          A_copia[i][j] = prom_vecinos
  #Algoritmo para determinar en que momento se llega al equilibrio térmico
  if(c_const > 0):
    for i in range (N+2):
      for j in range (N+2):
        if(A_copia[i][j]- A[i][j] < 0):
          if(A[i][j]-A_copia[i][j] <= tolerance):
            eq_value += 1.0
        else:
          if(A_copia[i][j]- A[i][j] <= tolerance):
            eq_value += 1.0
    if(float((eq_value)/((N+2)*(N+2)))==1.0):
      eq_total = 1
      print("El cuerpo alacnzo el equilibrio en la", c_const, "iteracion")
    else:
      eq_value = 0
  
  A = A_copia.copy()
  print("\n",A_copia,"\n")
  c_const += 1