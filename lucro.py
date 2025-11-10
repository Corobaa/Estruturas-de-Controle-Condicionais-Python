#Um comerciante quer vender os produtos que compra com as seguintes margens de lucro:
#- 45% de lucro se o valor da compra for inferior a 340,00Mt
#- 35% de lucro se o valor da compra for maior ou igual a 340,00Mt e menor do que 680,00
#- 25% de lucro se o valor da compra for maior ou igual a 680,00 Mt e menor do que 1020,00 Mt
#- 15% de lucro se o valor da compra for maior ou igual a 1020,00 Mt
valor_compra = float(input("Digite o valor da compra do produto em Mt: "))      
if valor_compra < 340.00:
    lucro = valor_compra * 0.45
    valor_venda = valor_compra + lucro
    print("O valor de venda do produto é: ",valor_venda)              
elif valor_compra >= 340.00 and valor_compra < 680.00:          
    lucro = valor_compra * 0.35
    valor_venda = valor_compra + lucro
    print("O valor de venda do produto é: ",valor_venda)               
elif valor_compra >= 680.00 and valor_compra < 1020.00:          
    lucro = valor_compra * 0.25
    valor_venda = valor_compra + lucro
    print("O valor de venda do produto é: ",valor_venda)            
else:          
    lucro = valor_compra * 0.15
    valor_venda = valor_compra + lucro
    print("O valor de venda do produto é:",valor_venda) 
print("o lucro obtido na venda é de:",lucro) 
print("Obrigado por usar o nosso sistema!")
    