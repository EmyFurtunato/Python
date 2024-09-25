print("Cálculo do IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = (peso / altura ** 2)

if imc <= 18.5:
    print("Você está abaixo do peso)")
elif imc > 18.5 or imc < 24.9:
    print("Você está no peso ideal")
elif imc > 25 and imc < 34.9:
    print("Sobrepeso")
else: print("Você está obeso")
print("Seu IMC é: ", imc)