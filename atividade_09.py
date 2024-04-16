#atividade_09
salario = float(input("Digite o salario do trabalhador: "))
valor_prestação = float(input("Digite o valor da prestação: "))
l_prestação = salario * 0.2

if valor_prestação > l_prestação:
    print("Emprestimo não concedido!")
else:
    print("Emprestimo concedido!")