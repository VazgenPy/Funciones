def rango(num1, num2):
    for i in range(num1 + 1, num2):
        l.append(i)
    return l


l = []
print(
    rango(num1=int(input("Dime el ultimo numero: ")),
          num2=int(input("Dime el primer numero: "))))
print(l)
