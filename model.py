import numpy as np

A = np.float_([30,30])
B = np.float_([40,40])
C = np.float_([0,0])
D = np.float_([0,0])

#while (A != B).all():
#    print("Hola 2")
#    C[1] = (A[0] + A[1] + B[0])/3
#    C[0] = (A[0] + A[1])/2
#    D[1] = (B[0] + B[1])/2
#    D[0] = (A[1] + B[0] + B[1])/3
#    print("A = ", C)
#    print("\n")
#    print("B =", D)
#    print("\n")
#    if (C != D).all():
#        print("Hola")
#        A[1] = (C[0] + C[1] + D[0])/3
#        A[0] = (C[0] + C[1])/2
#        B[1] = (D[0] + D[1])/2
#        B[0] = (C[1] + D[0] + D[1])/3
#        print("A = ", A)
#        print("\n")
#        print("B =", B)
#        print("\n")
#    else:
#        print("Los sistemas se encuentran en equilibrio térmico")
#else:
#    print("Los sistemas se encuentran en equilibrio térmico")
i = 0
while (A != B).all():
    i += 1
    C[1] = (A[0] + A[1] + B[0])/3
    C[0] = (A[0] + A[1])/2
    D[1] = (B[0] + B[1])/2
    D[0] = (A[1] + B[0] + B[1])/3
    if (C != D).all():
        A[1] = (C[0] + C[1] + D[0])/3
        A[0] = (C[0] + C[1])/2
        B[1] = (D[0] + D[1])/2
        B[0] = (C[1] + D[0] + D[1])/3
        print(A)
        print(B)
    else:
        print("A = ", A)
        print("B =", B)
        print("\n")
        print("El equilibrio térmico se alcanzó después de ", i, "iteraciones.")
        break
else:
    print("El sistema se encuentra en equilibrio térmico")
