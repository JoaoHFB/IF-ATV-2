nota_lab = float(input("Digite a primeira nota que tem peso 2: "))
nota_semestra = float(input("Digite a segunda nota que tem peso 3: "))
nota_ex_final = float(input("Digite a terceira nota que temo peso 5: "))

media = (nota_lab * 0.2) + (nota_semestra * 0.3) + (nota_ex_final * 0.5)

if media < 2.49:
    print("Está reprovado!")
elif media >= 2.5 and media < 4.9:
    print("Está de recuperação!")
else:
    print("Está aprovado!")
