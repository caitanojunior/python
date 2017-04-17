largura = int(input("Digite a largura: "))
altura =  int(input("Digite a altura: "))
i = 1

while i <= altura:
    if i == 1 or i == altura:
        print(largura * "#")
    else:
        print("#", (largura -4) * " ", "#")
    i = i + 1
