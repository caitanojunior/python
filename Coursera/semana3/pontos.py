import math

coordX1 = int(input('Digite a coordenada X1: '))
coordY1 = int(input('Digite a coordenada Y1: '))
coordX2 = int(input('Digite a coordenada X2: '))
coordY2 = int(input('Digite a coordenada Y2: '))

cateto1 = coordX2 - coordX1
cateto2 = coordY2 - coordY1

hipotenusa = (cateto1**2) + (coordY2**2)

distancia = math.sqrt(hipotenusa)

if(distancia >= 10):
    print('longe')
else:
    print('perto')
