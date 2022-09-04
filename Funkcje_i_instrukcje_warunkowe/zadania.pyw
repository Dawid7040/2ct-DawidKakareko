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
	result = 0
	sil = 1
	for i in range(1, n + 1):
		sil *= i

	sil = str(sil)

	for x in range(len(sil)-1, 1, -1):
		print(len(sil), x)
		if sil[x] != "0":
			return result
		result += 1
	return result

print(zadania3())
