def imprimir_meses(numero):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
        
    }
    if numero in meses:
        print("O mes correspondente ao número {} é {}".format(numero, meses[numero]))
    else:
        print("Número inválido. Por favor, insira um número entre 1 e 7.")
numero = int(input("Digite um número entre 1 e 12: "))
imprimir_meses(numero)