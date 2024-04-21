#Atividade_18

def verifica_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} é divisível por 3 e por 5.")
    elif numero % 3 == 0:
        print(f"{numero} é divisivel apenas por 3.")
    elif numero % 5 == 0:
        print(f"{numero} é divisivel apenas por 5.")
    else:
        print(f"não é divisivel nem por 3 nem por 5.")
numero = int(input("Digite um número inteiro: "))
resultado = verifica_divisibilidade(numero)
print(resultado)