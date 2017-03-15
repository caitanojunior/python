entrada = int(input('Digite um número inteiro: '))
numeroStr = str(entrada)

if(entrada < 100):
    dezena = entrada // 10
    print('O dígito das dezenas é', dezena)

elif(entrada < 1000):
    dezena = numeroStr[1:2]
    print('O dígito das dezenas é', dezena)

elif(entrada < 10000):
    dezena = numeroStr[2:3]
    print('O dígito das dezenas é', dezena)

elif(entrada < 100000):
    dezena = numeroStr[3:4]
    print('O dígito das dezenas é', dezena)

elif(entrada < 1000000):
    dezena = numeroStr[4:5]
    print('O dígito das dezenas é', dezena)

elif(entrada < 10000000):
    dezena = numeroStr[5:6]
    print('O dígito das dezenas é', dezena)

elif(entrada < 100000000):
    dezena = numeroStr[6:7]
    print('O dígito das dezenas é', dezena)

elif(entrada < 1000000000):
    dezena = numeroStr[7:8]
    print('O dígito das dezenas é', dezena)

elif(entrada < 10000000000):
    dezena = numeroStr[8:9]
    print('O dígito das dezenas é', dezena)

elif(entrada < 10000000000):
    dezena = numeroStr[9:10]
    print('O dígito das dezenas é', dezena)

elif(entrada < 100000000000):
    dezena = numeroStr[9:10]
    print('O dígito das dezenas é', dezena)

elif(entrada < 1000000000000):
    dezena = numeroStr[10:11]
    print('O dígito das dezenas é', dezena)
