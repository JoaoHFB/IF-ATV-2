hora_chegada = int(input("Digite a hora de chegada (0-23): "))
minuto_chegada = int(input("Digite os minutos de chegada (0-59): "))

hora_partida = int(input("Digite a hora de partida (0-23): "))
minuto_partida = int(input("Digite os minutos de partida (0-59): "))

tempo_chegada = hora_chegada * 60 + minuto_chegada
tempo_partida = hora_partida * 60 + minuto_partida
tempo_estacionamento = tempo_partida - tempo_chegada

if tempo_estacionamento <= 120:
    preco = 1.00 * 2
elif tempo_estacionamento <= 240:
    preco = 1.40 * 2
else:
    preco = 2.00 * ((tempo_estacionamento + 59) // 60)

print(f"O preço cobrado pelo estacionamento é R${preco:.2f}.")