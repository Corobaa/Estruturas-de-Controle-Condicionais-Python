#Escreva um programa para ler 3 notas de um aluno e informar se o aluno está aprovado, reprovado ou se
#deverá realizar o exame final.
#• O aluno será Aprovado a média de suas notas for > 14
#• O aluno será Reprovado se a média de suas notas for < 10
#• O aluno deverá realizar o exame se a média de suas notas for >= 10 e < 14

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
media=(nota1+nota2+nota3)/3
if media>14 :
    print("Aprovado")
elif media< 10:
    print(" Reprovado")
elif media>=10 and media <14:
    print(" Deve realizar o exame especial")
