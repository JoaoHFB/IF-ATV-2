#atividade_16

base_maior = float(input("Digite a base maior do trapezio: "))
base_menor = float(input("Digite a base menor do trapezio: "))
altura = float(input("Difite a altura do trapezio: "))

calcular_area = (base_maior + base_menor * altura) / 2
if base_menor < 0:
    print("digite um numero valido!")
elif base_maior < 0:
    print("Digite um numero valido")
else:
    print(f"A area vai ser {calcular_area}")