#Escreva um programa para ler 3 notas diferentes de um aluno e informar o valor da sua maior nota.
#Altere este programa para informar também se a maior nota foi a primeira, a segunda ou a terceira.
nota1= float(input(" Type your note 1:"))
nota2= float(input(" Type your note 2:"))
nota3= float(input(" Type your note 3:"))
if nota1>nota2 and nota1>nota3 :
    print("a sua maior nota foi a primeira ", nota1)
elif nota2>nota1 and nota2>nota3 :
    print("a sua maior nota foi a segunda ", nota2)
else:
    print("A sua maior nota foia a tercira",nota3)