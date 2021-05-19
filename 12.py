import random
import math as ma


def deteccion_de_numero(num1, num2):
    if (not num1.isnumeric()) or (not num2.isnumeric()):
        return (False)
    else:
        return (True)


def deteccion_de_tres_numeros(num1 , num2, num3):
	if (not num1.isnumeric()) or (not num2.isnumeric()) or (not num3.isnumeric()):
		return (False)
	else:
		return(True)


def deteccion_de_solo_un_numero(num1):
	if (not num1.isnumeric()):
		return(False)
	else:
		return(True)
		

def suma(numero1, numero2):
    return int(numero1) + int(numero2)


def resta(numero1, numero2):
    return int(numero1) - int(numero2)


def multiplicar(numero1, numero2):
    return int(numero1) * int(numero2)


def divisio(numero1, numero2):
    try:
        return (int(numero1) / int(numero2))
    except ZeroDivisionError:
        return (False)


def aleatori(inici, final):
    try:
        return random.randint(int(inici), int(final))
    except ValueError:
        return False


def arrelQuadrada(numero):
    return ma.sqrt(int(numero))


def potencia(base, exponent):
    return int(base)**int(exponent)


def factorial(numero): 
    resultado = 1
    i = 1
    while i <= int(numero):
        resultado = resultado * i
        i = i + 1
    return resultado


def eq_segundo_grado(a , b , c):
	return("El resultado es: " , (-(int(b))+ma.sqrt(int(b)**2-4*int(a)*int(c)))/2*int(num1))

#Codi principal de la calculadora
opcio = 0
while (opcio != 10):
	print("CALCULATOR CREATED BY VAZGEN")
	print("1- Sum")
	print("2- Subtract")
	print("3- Multiply")
	print("4- Divide")
	print("5- Random number")
	print("6- Square root")
	print("7- Powers")
	print("8- Factorial")
	print("9- Eq. Second Grade")
	print("10- Exit")
	opcio = int(input("Quina opció entres? "))

	if (opcio == 1):
		print("Entra els dos números a sumar")
		num1 = input("Entra el primer número: ")
		num2 = input("Entra el segon número: ")
		if deteccion_de_numero(num1, num2) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(suma(num1, num2))
		print("----------------------------------------------")

	elif (opcio == 2):
		print("Entra els dos números a restar")
		num1 = input("Entra el primer número: ")
		num2 = input("Entra el segon número: ")
		if deteccion_de_numero(num1, num2) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(resta(num1, num2))
		print("----------------------------------------------")

	elif (opcio == 3):
		print("Entra els dos números a multiplicar")
		num1 = input("Entra el primer número: ")
		num2 = input("Entra el segon número: ")
		if deteccion_de_numero(num1, num2) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(multiplicar(num1, num2))
		print("----------------------------------------------")

	elif (opcio == 4):
		print("Entra els dos números a dividir")
		numerador = input("Entra el primer número: ")
		denominador = input("Entra el segon número: ")
		if deteccion_de_numero(numerador, denominador) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		if divisio(numerador, denominador) == False:
			print("No se puede dividir entre 0")
			print("----------------------------------------------")
			continue
		print(divisio(numerador, denominador))
		print("----------------------------------------------")

	elif (opcio == 5):
		print("Entra els dos números entre els que vols el nombre aleatori")
		inici = input("Entra el primer número: ")
		fi = input("Entra el segon número: ")
		if deteccion_de_numero(inici, fi) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		if aleatori(inici, fi) == False:
			print("El primer numero no puede ser mas grande que el segundo")
			print("----------------------------------------------")
			continue
		print(aleatori(inici, fi))
		print("----------------------------------------------")

	elif (opcio == 6):
		print("Entra el número del que vols l'arrel quadrada")
		num1 = input("Entra el número: ")
		if deteccion_de_solo_un_numero(num1) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(arrelQuadrada(num1))
		print("----------------------------------------------")

	elif (opcio == 7):
		b = input("Entra la base: ")
		e = input("Entra l'exponent: ")
		if deteccion_de_numero(b, e) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(potencia(b, e))
		print("----------------------------------------------")

	elif (opcio == 8):
		num = input("Entra el numero: ")
		if deteccion_de_solo_un_numero(num) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(factorial(num))
		print("----------------------------------------------")
	
	elif (opcio == 9):
		num1 = input("Number raised to 2: ")
		num2 = input("Number raised to 1: ")
		num3 = input("Independent number: ")
		if deteccion_de_tres_numeros(num1 , num2 , num3) == False:
			print("It's not a number, please try again")
			print("----------------------------------------------")
			continue
		print(eq_segundo_grado(num1 , num2 , num3))
		print("----------------------------------------------")

	elif (opcio < 1 or opcio > 10):
		print("That option doesn't exits, please try again")
		print("----------------------------------------------")
		continue

print("\033[0;32m" , "Bye, have a good day!\n" , "Follow me on Instagram: https://www.instagram.com/_vazgen_vk/")
