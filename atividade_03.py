#atividade 3
import math

numero = float(input("Digite um numero real: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz do numero {numero} é: {raiz}")
else:
    quadrado = numero ** 2
    print(f"O quadrado do numero {numero} é: {quadrado}")