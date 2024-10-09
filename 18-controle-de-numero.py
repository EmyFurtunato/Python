# ferramenta controla a exibição de uma sequência de números

contador = 0

while contador <= 100:
    contador += 1

    # no lugar dos números 6, 10 e 27 o código vai pular 
    if (contador == 6):
        print("não vou mmostrar o número 6") # se for número 6 não vai mostrar
        continue # interrompe a interação atual e volta para o início do loop
    if (contador >= 10 and contador <= 27):
        print("não vou mmostrar") # se for de 10 até 27 não vai mostrar
        continue # interrompe a interação atual e volta para o início do loop

     # imprime o valor do contador
    print(contador)

    # ao chegar no 40, o programa vai encerrar
    if contador == 40:
        break # para a execução do while, sai do loop de repetição

print ("Fim do programa!!!!")

