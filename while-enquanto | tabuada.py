#While = condição
#Bloco de código | Atualização de condição
#Criar um algoritmo que imprime a tabuada de um número fornecido pelo usuário, utilizando o loop while

número = int(input("Digite um número: "))
contador = 0

while(contador<=10): 
    resultado = número * contador
    print(f"{número} x {contador} = {resultado}")
    contador+=1
