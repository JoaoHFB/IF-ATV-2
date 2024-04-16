#atividade 4

import math

numero = float(input("Digite um número: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    quadrado = numero ** 2
    print(f"Se o numero for positivo sua raiz será {raiz} e o seu quadarado será {quadrado}")
else:
    print("Digite um numero valido!")