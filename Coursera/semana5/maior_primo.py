def maior_primo(k):
    i = 2
    ehprimo = True

    while i <= k:
        if ((i // 2 != i/2 and i // 3 != i/3) or (i==2) or (i == 3)):
            maiorPrimo = i
        i=i+1
    return maiorPrimo
