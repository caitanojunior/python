import math
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

# delta = b² - 4ac
def calcDelta (a, b, c):
    return b**2 - 4*a*c

def bhaskara():
    return (-b + math.sqrt(calcDelta(a, b, c))) / (2 * a)


if(calcDelta(a, b, c) == 0):
    bhaskara()
    print('a raiz desta equação é', bhaskara())
else:
    if(calcDelta(a, b, c) < 0):
        print('esta equação não possui raízes reais')
    else:
        bhaskara()
        raiz2 = (-b - math.sqrt(calcDelta(a, b, c))) / (2 * a)
        if(bhaskara() < raiz2):
            print('as raízes da equação são',bhaskara(), 'e', raiz2)
        else:
            print('as raízes da equação são', raiz2, 'e', bhaskara())