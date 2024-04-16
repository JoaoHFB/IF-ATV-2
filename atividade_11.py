#atividade_11
import math

numero = int(input("Digite um numero inteiro: "))
if numero < 0:
    print("Numero invalido: ")
else:
    resultado = math.log(numero)
    print(f"O logaritimo do numero {numero} será: {resultado}")
    