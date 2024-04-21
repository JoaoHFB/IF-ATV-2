#atividade_14
def imprimir_dia_semana(numero):
    dias_da_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    if numero in dias_da_semana:
        print("O dia correspondente ao número {} é {}".format(numero, dias_da_semana[numero]))
    else:
        print("Número inválido. Por favor, insira um número entre 1 e 7.")
numero = int(input("Digite um número entre 1 e 7: "))
imprimir_dia_semana(numero)