#Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano.
#Faça um programa que, para o saldo médio de 3.500,00Mt de um cliente, calcule o valor do crédito e
#mostre uma mensagem informando o saldo médio e o valor do crédito de acordo com as condições
#abaixo:
#• Saldo médio Percentual de 0 a 200 nenhum crédito,
#• Saldo de 201 a 400 terá 20% do valor do saldo médio,
#• Saldo de 401 a 600 terá 30% do valor do saldo médio, e
#• Saldo acima de 601 40% do valor do saldo médio.
saldo_medio =3500;
print("O seu saldo medio",saldo_medio)
if saldo_medio>0 and saldo_medio<=200:
    print("Nao tem direito ao credito")
elif saldo_medio>=201 and saldo_medio<=400:
    credito=saldo_medio*0.20;
    print("O seu credito",credito,"")
elif saldo_medio>=401 and saldo_medio<=600:
    credito=saldo_medio*0.30;
    print("O seu credito",credito,"")
    
elif saldo_medio> 601:
    credito=saldo_medio*0.40;
    print("O seu credito",credito,"")
    
