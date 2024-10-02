# Declaração da função exibirMensagem(nome)
def exibirMensagem(nome):
    print(f"Olá, {nome}!!!")


def somar(a, b):
    return a + b


def calcularareadocirculo(raio):
    area = 3.1415 * raio**2
    return area


# Início do meu algoritmo
nome = input("Digite seu nome:")
exibirMensagem(nome)


# chamando função com retorno
valorA = int(input("Digite o primeiro número: "))
valorB = int(input("Digite o segundo número: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")

# calculando a área do circulo
print("Área do círculo")
raio = float(input("Digite o valor do raio: "))
area = calcularareadocirculo(raio)
print(f"A Área do círculo: {area:.2f}")