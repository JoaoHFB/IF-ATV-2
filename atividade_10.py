import math

numero = int(input("Digite um numero inteiro maior do que zero: "))
if numero <= 0:
    print("numero invalido!")
else:
    soma = 0
    for digito in str(numero):
        soma += int(digito)
print(f"A soma dos digitos é: {soma}")