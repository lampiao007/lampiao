# Voto obrigatório

nome = input("Qual o seu nome? ")
idade = float(input("Quantos anos você tem? "))

if (idade>=18 and idade<=64):
    print(nome, "seu voto é obrigatório.")
elif (idade>=16 and idade<18 or idade>64):
    print (nome, "seu voto é opcional.")
else:
    print (nome, "você não pode votar.")
