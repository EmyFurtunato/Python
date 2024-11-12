# NESSE CÓDIGO O USUÁRIO DESCOBRE O VALOR DO INGRESSO
# POR MEIO DA INFORMAÇÃO DE SE É OU NÃO ESTUDANTE


print("DESCUBRA O VALOR DO SEU INGRESSO!") 

# Início do meu algorítmo
valor_inteira = 20
valor_meia = 10

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print("Digite 2 se não for estudante, digite 1 se for")
estudante_ou_inteira = int(input("Você é estudante ou não? "))

if estudante_ou_inteira == 1:
    print("O seu ingresso vale R$10,00")

elif estudante_ou_inteira == 2:
    print("O seu ingresso vale R$20,00")

print("TENHA UM BOM FILME!")