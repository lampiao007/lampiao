#Desenvolver um programa que solicita ao usuário um número, e em seguida, calcula a soma de todos os números pares até esse número, utilizando loop while

número = int(input("Digite um número par: "))
limite = 0

if(número%2==0):
    while(limite<=20): 
        n2 = número + limite
        print(f"{número} + {limite} = {n2}")
        limite+=2
else:
    print("Esse número não é par.")
