from http.client import NETWORK_AUTHENTICATION_REQUIRED
import time
def zadanie0(left, right):
    def f(x):
        return 2 * x - 4

    def zeroplace(l,r):
        s = (l+r)/2
        while f(s) != 0:
            time.sleep(0.2)
            print(s)
            if f(l)*f(s) < 0:
                l = s
            else:
                r = s
            s = (l+r)/2
        return s
    print(zeroplace(left, right))


def zadanie1(number):
    times = 0
    while number > 0:
        times += 1
        for i in str(number):
            number -= int(i)
    return number, times

def reventnumber():
    while True: 
        number = int(input("Podaj liczbę dodatnią: "))  
        if not number < 0: return number     

reventnumber()