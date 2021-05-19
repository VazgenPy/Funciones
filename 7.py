l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def eliminar(l):
    for i in range(len(l)):
        if 3 in l:
            l.remove(3)
        elif 5 in l:
            l.remove(5)
        elif 7 in l:
            l.remove(7)
    print(l)


eliminar(l)
