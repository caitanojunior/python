segundo = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dia = 0
hora = 0
minuto = 0

if(segundo < 60):
    print(dia, 'dias,', hora, 'horas,', minuto, 'minutos e', segundo, 'segundos.')
elif(segundo <3600):
    minuto = segundo//60
    segundo = segundo%60
    print(dia, 'dias,', hora, 'horas,', minuto, 'minutos e', segundo, 'segundos.')
elif(segundo < 86400):
    hora = segundo //3600
    minuto = segundo%3600 //60
    segundo = segundo%3600//60
    print(dia, 'dias,', hora, 'horas,', minuto, 'minutos e', segundo, 'segundos.')
else:
    dia = segundo//86400
    temp1 = segundo%86400 #temp vale 12310
    hora = temp1//3600
    temp2 = temp1%3600
    minuto = temp2//60
    segundo = temp1%60
    print(dia, 'dias,', hora, 'horas,', minuto, 'minutos e', segundo, 'segundos.')

