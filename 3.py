def relaciona(a,b):
	if a > b:
		return 1
	elif a < b:
		return -1
	else:
		return 0
print(relaciona(int(input("Dime el primer numero: ")) , int(input("Dime el segundo numero: "))))