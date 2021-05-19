import os
l = []
#Definicion de Funciones:
def cls():
	os.system("cls" if os.name == "nt" else "clear")

def Crear_Lista():
	primero = input("Nom: ")
	segundo = input("Ingredient Principal: ")
	tercero = int(input("Calorias: "))
	cuarto = int(input("Dificauldad (Del 0 al 5): "))
	quinto = input("Explicacion: ")
	l.append([primero,segundo,tercero,cuarto,quinto])

def Borrar():
	b = int(input("Que elemento quieres eliminar: "))
	l.remove(l[b-1])

def Actualizar():
	e = int(input("Que elemento quieres: "))
	f = int(input("Que componente quieres: "))
	g = input("Que quieres poner: ")
	l[e-1][f-1] = g

def Buscar():
	receta = input("Dime el nombre de la receta: ")
	lista_nueva = []
	falso = False
	for elemento in l:
		for componente in elemento:
			if receta == componente:
				lista_nueva = elemento
				falso = True
	if falso:
		print(lista_nueva)
	else:
		print("No existe")

#Programa
while True:
	a = input("Que quieres hacer (Insertar , Mostrar , Eliminar , Actualizar , Buscar o Salir): ")
	if a == "Insertar" or a == "insertar":
		Crear_Lista()
		input("Borrar")
		cls()
	elif a == "Mostrar" or a =="mostrar":
		for a in range(len(l)):
			print(l[a])
		input("Borrar")
		cls()
	elif a == "Eliminar" or a == "eliminar":
		Borrar()
		input("Borrar")
		cls()
	elif a == "Actualizar" or a == "actualizar":
		Actualizar()
		input("Borrar")
		cls()	
	elif a == "Buscar" or a == "buscar":
		Buscar()
		input("Borrar")
		cls()
	elif a == "Salir" or a == "salir":
		print("Adios")
		cls()
		break