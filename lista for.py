#Crie uma lista de 5 números inteiros fernecidos pelo usuário e imprima o maior, o menor e a soma de todos os elementos.

numeros = []
print("#LISTA DE NÚMEROS#")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))
n5 = int(input("Digite um número: "))

numeros = [n1, n2, n3, n4, n5]
maior= max(numeros)
menor= min(numeros)
soma = sum(numeros)

print(f"\nO maior número da sua lista é: {maior}") 
print(f"O menor número da sua lista é: {menor}")
print(f"A soma de todos os números da lista é: {soma}")
