#Exibir a soma dos números pares de 1 a 50
soma = 0
for i in range(50):
    if i%2==0:
        soma += i
print(soma)
