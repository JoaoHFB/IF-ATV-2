#Atividade 02
import math

numero = float(input("Digite um numero: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    
    print(f"A raiz quadrado do numero {numero} é: {raiz}")
else:
    print("Numero invalido, por favor digite outro numero.")
    