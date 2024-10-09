# ferramenta continue
# a ferramenta continue no python vai começar a interromper o loop,
# mas vai dar continuidade a ele.

contador = 0

while contador <= 40:
    contador += 1

    # verifica se o valor de 'contador' é múltiplo de 4
    if (contador % 4 == 0):
        print("pim") # se for múltiplo de 4, imprime "pim"
        continue # interrompe a interação atual e volta para o início do loop

    # se o número não for multiplo de 4, imprime o valor do contador
    print(contador)
# após o término do loop, imprime a mensagem de finalização
print("fim  do programa")