#atividade_08
nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))

if 0.0 <= nota_01 <= 10.0 and 0.0 <= nota_02 <= 10.0:
    media = (nota_01 + nota_02) / 2
    print(f"A media do aluno será: {media}")
else:
    print("A nota é invalida!")
    print("Para a nota ser valida preciso que digite um valor entre 0.0 e 10.0.")