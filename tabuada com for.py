#Exibir a tabuada de um número inserido na tela
x = int(input("Qual o número da tabuada? "))
for i in range(11):
    print(f"{x} x {i} = {x*i}")
