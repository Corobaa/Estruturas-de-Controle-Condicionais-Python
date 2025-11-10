#11. Para cada produto informado (nome, preço e quantidade), escreva o nome do produto comprado e o
#valor total a ser pago, considerando que são oferecidos descontos pelo número de unidades compradas,
#segundo a tabela abaixo:
#a. Ate 10 unidades: valor total
#b. de 11 a 20 unidades: 10% de desconto
#c. de 21 a 50 unidades: 20% de desconto
#d. acima de 50 unidades: 25% de desconto
nome_produto = input("Digite o nome do produto: ")
preco= float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
valor_apagar=preco*quantidade
if quantidade>=10 :
    print("O valor a pagar",valor_apagar)
elif quantidade>11 and quantidade<20 :
    valor=valor_apagar-(valor_apagar*0.10)
    print("O Valor a pagar",valor)
elif quantidade>21 and quantidade<50 :
    valor=valor_apagar-(valor_apagar*0.20)
    print("O Valor a pagar",valor)
elif quantidade>50 :
    valor= valor_apagar-(valor_apagar*0.25)
    print("O Valor a pagar",valor)
    
print("------",nome_produto,"----------")