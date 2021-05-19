def contar(t , n):
	grafia = []
	total = 0
	for i in range(n):
		grafia.append(input("Dime la grafia: "))
	for a in range(len(grafia)):
		total = t.count(grafia[a])	
		print("Hay" , total , grafia[a])



contar(input("Dime el texto: ") , int(input("Dime cuantas grafias quieres: ")))