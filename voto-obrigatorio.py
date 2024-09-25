print("Bem vindo a votação 2024!")

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65:
    print("Voto obrigatorio")
elif idade >= 16 and idade <= 17 or idade >= 65:
    print("Voto opcional")
else:
    print("Voto não permitido")