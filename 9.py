def recogida():
	l = []
	for i in range(2):
		print("Estas rellenando la lista" , var + 1 , ": ")
		l.append(int(input()))
	print(" ")
	return l


def comparar(a,b):
	for i in a:
		for j in b:	
			if i == j:
				return True
	return False


#Recogida de datos
ListaGeneral = []
NumListas = int (input("¿Cuántas listas quieres comparar?"))
for var in range(NumListas):
	ListaGeneral.append(recogida())


#Comparación Listas
for i in range(len(ListaGeneral)):
	for j in range(i+1 , len(ListaGeneral)):
		if comparar(ListaGeneral[i] , ListaGeneral[j]):
			print("Hay coincidencia")
			exit()
print("No hay coincidencia")
exit()
