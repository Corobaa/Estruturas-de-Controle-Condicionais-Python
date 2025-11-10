#Crie uma variável contendo a idade de uma pessoa e verifique sua classe eleitoral: (até 16 anos não pode
#votar); (entre 16 e 18 anos ou mais que 65 é facultativo); (entre 18 e 65 anos é obrigatório).
print("Classe Eleitoral")
idade = int(input("Quantos anos tu tens?"))
if idade<= 16 :
    print("Nao pode votar")
elif idade>=16 and idade<18 or idade> 65 :
    print("Facultativo")
elif idade>= 18 and idade<=65 :
    print("Obrigatorio")
