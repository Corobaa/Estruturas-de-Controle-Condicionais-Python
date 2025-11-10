# Crie três variáveis inteiras e um trecho de código que descubra a maior entre elas. Imprima as três
#variáveis em ordem crescente.
nr1 = int(input("Introduza o primeiro número inteiro: "))
nr2 = int(input("Introduza o segundo número inteiro: "))
nr3 = int(input("Introduza o terceiro número inteiro: "))
if nr1 <= nr2 and nr1 <= nr3:
    if nr2 <= nr3:
        print("Números em ordem crescente: ", nr1, nr2, nr3)
    else:
        print("Números em ordem crescente: ", nr1, nr3, nr2)    