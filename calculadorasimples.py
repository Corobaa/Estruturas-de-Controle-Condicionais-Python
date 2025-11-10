nr1 = float(input("Type the first number: "))
nr2 = float(input("Type the second number: "))
escolha = input("Choose the operator (+, -, *, /): ")
if escolha == "+":
    resultado = nr1 + nr2
    print("Soma:", resultado)
elif escolha == "*":
    resultado = nr1 * nr2
    print("Multiplica:", resultado)
elif escolha == "-":
    resultado = nr1 - nr2
    print("Subtrai:", resultado)
elif escolha == "/":
    if nr2 != 0:
        resultado = nr1 / nr2
        print("Dividir:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operador inválido. Escolha +, -, *, ou /.")

