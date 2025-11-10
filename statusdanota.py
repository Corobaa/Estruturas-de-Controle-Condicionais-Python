#Escreva um programa que verifique se uma nota é péssima (nota=1), ruim (2), regular (3), boa (4),
#ótima (5) ou nenhuma delas (nota inválida).
nota = int(input("Introduza a sua nota: "))
if nota == 1:
    print("nota péssima")
elif nota == 2:
    print("nota ruim")
elif nota == 3:
    print("nota regular")
elif nota == 4:
    print("nota boa")
elif nota == 5:
    print("nota ótima")
else:
    print("nota inválida")
