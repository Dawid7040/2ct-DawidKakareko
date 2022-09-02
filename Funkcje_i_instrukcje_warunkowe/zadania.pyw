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
	n = int(input("Podaj liczbe: "))
	if n > 2000000 or n < 1:
		return 0
	
	i = int(n/5)
	
	i = i + (int(n/25))

	return i
		