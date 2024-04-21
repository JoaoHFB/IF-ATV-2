#atividade_19

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A < B + C and B < A + C and C < A + B:
    if A == B == C:
        print("triangulo equilatero!")
    elif A == B or A == C or B == C:
        print("Triangulo isoceles!")
    else:
        print("Triangulo escaleno!")
else:
    print("Os valores não são um triangulo")