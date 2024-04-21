#Atividade_21

taxas_imposto = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite a sigla do estado destino (MG, SP, RJ, MS): ").upper()

if estado_destino in taxas_imposto:
    imposto = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + imposto)
    print(f"O preço final do produto para o estado {estado_destino} é: R${preco_final:.2f}")
else:
    print("Erro: Estado destino inválido.")