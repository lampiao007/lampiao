#Calculadora com escolha do usuário#
opcao = 0

while True:

    print(" ")
    print("######## MENU DA CALCULADORA #########")
    print("**************CATÁLOGO:**************")
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. Resto da divisão")
    print("6. Potencia")
    print("7. sair")

    opcao = int(input("Escolha sua opção: "))

    if (opcao) in [1]:
        valorA = int(input("Digite um valor: "))
        valorB = int(input("Digite um valor: "))
        print(f"{valorA} + {valorB} = {valorA + valorB}")

    elif (opcao) in [2]:
        valorA = int(input("Digite um valor: "))
        valorB = int(input("Digite um valor: "))
        print(f"{valorA} - {valorB} = {valorA - valorB}")

    elif (opcao) in [3]:
        valorA = int(input("Digite um valor: "))
        valorB = int(input("Digite um valor: "))
        print(f"{valorA} x {valorB} = {valorA * valorB}")

    elif (opcao) in [4]:
        valorA = int(input("Digite um valor: "))
        valorB = int(input("Digite um valor: "))
        print(f"{valorA} : {valorB} = {valorA / valorB}")

    elif (opcao) in [5]:
        valorA = int(input("Digite um valor: "))
        valorB = int(input("Digite um valor: "))
        print(f" O resto da divisão de {valorA} por {valorB} é igual a {valorA // valorB}")

    elif (opcao) in [6]:
        valorA = int(input("Digite um valor: "))
        valorB = int(input("Digite um valor: "))
        print(f"{valorA} elevado a {valorB} = {valorA ** valorB}")

    elif (opcao) in [7]:
        print("Finalizando...")
        break

    else:
        print("Essa opção não é permitida, tente outra!")
