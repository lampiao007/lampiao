def exibirMenu():
    print("****CONVERSOR DE TEMPERATURA****")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Celsius para Kelvin")
    print("3. Converter de Fahrenheit para Celsius")
    print("4. Converter de Fahrenheit para Kelvin")
    print("5. Converter de Kelvin para Celsius")
    print("6. Converter de Kelvin para Fahrenheit")
    print("7. Finalizar código.")

    select = int(input("O que você quer converter? "))
    return select

def celsius_fahrenheit(C):
    return ((9*C)/5) + 32
def celsius_kelvin(C):
    return  C + 273
def fahrenheit_celcius(F):
    return (5*(F-32))/9
def fahrenheit_kelvin(F):
    return (F - 32)*5/9 + 273
def kelvin_celsius(K):
    return K - 273
def kelvin_fahrenheit(K):
    return (K - 273)*9/5 + 32

while True:
    select = exibirMenu()
    if select == 1:
        print("- Selecionando opção 1 -\n")
        C = float(input("Qual a temperatura em Celsius? "))
        F = celsius_fahrenheit(C)
        print(f"O valor de Fahrenheit é: {F}F\n")  

    elif select == 2:
        print("- Selecionando opção 2 -\n")
        C = float(input("Qual a temperatura em Celsius? "))
        K = celsius_kelvin(C)
        print(f"O valor de Kelvin é: {K}K\n")

    elif select == 3:
        print("- Selecionando opção 3 -\n")
        F = float(input("Qual a temperatura em Fahrenheit? "))
        C = fahrenheit_celcius(F)
        print(f"O valor de Celcius é: {C}°C\n")  

    elif select == 4:
        print("- Selecionando opção 4 -")
        F = float(input("Qual a temperatura em Fahrenheit? "))
        K = fahrenheit_kelvin(F)
        print(f"O valor de Kelvin é: {K}K\n") 
        
    elif select == 5:
        print("- Selecionando opção 5 -")
        K = float(input("Qual a temperatura em Kelvin? "))
        C = kelvin_celsius(K)
        print(f"O valor de Celcius é: {C}°C\n") 

    elif select == 6:
        print("- Selecionando opção 6 -")
        K = float(input("Qual a temperatura em Kelvin? "))
        F = kelvin_fahrenheit(K)
        print(f"O valor de Fahrenheit é: {F}F\n") 

    elif select == 7:
        print("Finalizando programa...")
        break
    
    else: 
        print("Opção inválida. Por favor, tente novamente.\n")
