def zadanie1():
	x = int(input("Podaj wartosc: "))
	if x < 17:
		return x - 17
	else:
		return abs(2*(x - 17))



def zadanie2():
	n = int(input("Podaj liczbe: "))
	if n > 2000000 or n < 1:
		return 0

	silnia = 1
	for x in range(1,n+1):
		print(x)
		silnia = x * silnia
	
	str_silnia = str(silnia)
	return str_silnia[-1]

def zadania3():
	user_input = int(input("Podaj liczbe: ")) 
	dzielniki = []
	for current in range(1,100000):
		result = 5
		for x in range(1, current):
			result *= 5
		if result > user_input:
			break
		dzielniki.append(result)
	result = 0
	for dziel in dzielniki:
		result = result + ( user_input / dziel ) 
	return F"{int(result)} Ilosc zer"



print(zadania3())