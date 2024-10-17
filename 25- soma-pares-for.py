# ALGORÍTMO FEITO POR BRUNNA, EMILLY E THIFANNY DO 2F-DS

soma = 0

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        soma += i 

print(f"A soma dos números pares entre 1 e 50 é: {soma}")