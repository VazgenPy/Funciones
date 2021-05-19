'''
l = []
for i in range(2):
	l.append(input("Dime una palabra:"))

for i in range(len(l)):
	for a in range(len(l)-1):
		print(l[i][a])


a = input("Dime las palabras: ")

b = a.find(" ")

print(a[0] , a[b+1])

------------------------------------------------------------

def iniciales(l):
	print(l[0])
	for i in range(len(l)):	
		if l[i] == " ":
			print(l[i + 1])
		else:
			continue


iniciales("hola que tal estas compañero")



-------------------------------------------------------------



def punt(l , g):
	return l.count(g)


print(punt(input("Dime el texto: ") , input("Dime la grafia")))


'''



def punt(l , g):
	a = 0
	for i in l:
		if i == g:
			a = a+1
	return a



print(punt(input("Dime el texto: ") , input("Dime la grafia: ")))
