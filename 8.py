def datos():
    Primera_Lista = []
    for i in range(5):
        Primera_Lista.append(int(input("Dime un numero para la lista: ")))
    print(Primera_Lista)
    return Primera_Lista


def comun(l, w):
    for i in range(len(l)):
        if l[i] in w:
            print(True)
            break
    for a in range(len(l)):
        if l[i] not in w:
            print(False)
            break


comun(datos(), datos())
