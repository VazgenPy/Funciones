l = []


def Separar_Listas(listas):
    pares = []
    senar = []
    for i in listas:
        if i % 2 == 0:
            pares.append(i)
            pares.sort
        elif i % 2 != 0:
            senar.append(i)
            senar.sort
    return senar, pares


for i in range(10):
    l.append(int(input("Añade un numero: ")))
print(Separar_Listas(l))
