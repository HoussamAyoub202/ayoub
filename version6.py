def swap(a, b):
    return b, a

A = int(input("Entrez la valeur de A : "))
B = int(input("Entrez la valeur de B : "))
A, B = swap(A, B)
print("Après l'échange, A =", A, "et B =", B)
