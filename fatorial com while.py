#Criar um programa que calcule o fatorial de um número fornecido pelo usuário usando um loop while

numero = int(input("Digite um número: "))
fatorial = 1
contador=1

while(contador<=numero): 
    fatorial = fatorial * contador
    contador = contador + 1
    
print(f"O fatorial de {numero} é {fatorial}")
