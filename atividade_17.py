#atividade_17

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

def mostrar_menu():
    print("Escolha a operação matemática:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def realizar_operacao(operacao, a, b):
    if operacao == 1:
        resultado = soma(a, b)
    elif operacao == 2:
        resultado = subtracao(a, b)
    elif operacao == 3:
        resultado = multiplicacao(a, b)
    elif operacao == 4:
        resultado = divisao(a, b)
    else:
        resultado = "Opção inválida."
    return resultado

mostrar_menu()
operacao = int(input("Digite o número da operação desejada: "))
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

resultado = realizar_operacao(operacao, valor1, valor2)
print("O resultado da operação é:", resultado)