import numpy as np

TA = float(input("Temperatura del cuerpo A: "))
TB = float(input("Temperatura del cuerpo B: "))
A = np.full((4, 4), TA)
B = np.full((4, 4), TB)
print("\n")
print(A)
print("\n")
print(B)
print("\n")

uniones = [[(0,0), (1,0), (2,0), (3,0), (0,0)], ]

