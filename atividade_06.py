#Atividade 06
numero_1 = int(input("Digite um numero inteiro: "))
numero_2 = int(input("Digite o segundo numero inteiro: "))

if numero_1 > numero_2:
    dif = numero_1 - numero_2
    print(f"O numero {numero_1} é maior")
    print(f"A Diferença entre eles é de {dif}")
elif numero_2 > numero_1:
    diferença = numero_2 - numero_1
    print(f"O numero {numero_2} é maior")
    print(f"A Diferença entre eles é de {diferença}")
else:
    print("Os numeros são iguais!")