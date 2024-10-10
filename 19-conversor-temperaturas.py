# o algoritmo converte as temperaturas entre as escalas Celsius, Fahrenheit e Kelvin

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

print("Oii, bem vindo ao conversor de temperaturas!")

nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Escolha a conversão que você deseja\n")

print("Celsius para Fahrenheit, digite 1 ")
print("Fahrenheit para Celsius, digite 2 ")
print("Celsius para Kekvin, digite 3 ")
print("Kekvin para celsius, digite 4 ")
print("Fahrenheit para Kelvin, digite 5 ")
print("Kelvin para Fahrenheit, digite 6")
print("Sair do programa 7\n ")

while True:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 7:
        print("Saindo do programa...")
        break
    temp = float(input("Insira a temperatura: "))
    if opcao == 1:
        print(f"{temp} °F é igual a: {fahrenheit_to_kelvin(temp):.2f} K")
    elif opcao == 2:
        print(f"{temp} °F é igual a: {fahrenheit_to_celsius(temp):.2f} °C")
    elif opcao == 3:
        print(f"{temp} K é igual a: {kelvin_to_fahrenheit(temp):.2f} °F")
    elif opcao == 4:
        print(f"{temp} K é igual a: {kelvin_to_celsius(temp):.2f} °C")
    elif opcao == 5:
        print(f"{temp} °C é igual a: {celsius_to_fahrenheit(temp):.2f} °F")
    elif opcao == 6:
        print(f"{temp} °C é igual a: {celsius_to_kelvin(temp):.2f} K")
    else:
        print("Opção inválida, tente novamente!")







