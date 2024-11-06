#Desenvolver um programa que solicita ao usuário um número, e em seguida, calcula a soma de todos os números pares até esse número, utilizando loop while

limite = int(input("Digite um número: "))
contador = 0
soma = 0

while(contador<=limite): 
        soma = soma + contador
        contador+=2

print(f"A soma dos pares até {limite} = {soma}")
