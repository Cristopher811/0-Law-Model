import numpy as np

def eqt(A, B, C, D):
    while
    if(A[0][3]):
        C[0][3] = (A[0][3] + B[0][0] + A[1][3] + A[0][2])/4
    if(B[0][0]):
        D[0][0] = (B[0][0] + B[0][1] + B[1][0] + A[0][3])/4
    if(A[1][3]):
       C[1][3] = (A[1][3] + A[0][3] + A[1][2] + A[2][3] + B[1][0])/5
    print(C)
    print("\n")
    print(D)
    print("\n")

TA = input("Temperatura del cuerpo A: ")
TB = input("Temperatura del cuerpo B: ")
TA = float(TA)
TB = float(TB)
A = np.full((4, 4), TA)
B = np.full((4, 4), TB)
C = np.full((4, 4), 0.0)
D = np.full((4, 4), 0.0)
print("\n")
print(A)
print("\n")
print(B)
print("\n")

eqt(A,B,C,D)
