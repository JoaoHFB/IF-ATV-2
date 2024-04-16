#Atividade_12
import math

nota_1 = float(input("Digite a primeira nota do aluno que tem peso 1: "))
peso1 = float(input("Digite o peso da primeira prova: "))
nota_2 = float(input("Digite a segunda nota do aluno que tem peso 2: "))
peso_2 = float(input("Digite o peso da segunda prova: "))
media = (nota_1*peso1 + nota_2*peso_2) / (peso1+peso_2)
if media >= 70:
    print(f"A media ponderada o aluno é {media} e ele foi aprovado.")
else:
    print(f"A media ponderada do aluno é {media} e ele não foi aprovado.")