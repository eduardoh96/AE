# Programa para análise de consumo de energia limpa

# Solicita o número de dias

while True:
    try:
        n = int(input("Insira a quantidade de dias para a coleta de dados de consumo de energia: "))
        if n == 0:
            print("Por favor, insira um valor maior que zero.")
            continue
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")

# Variáveis para armazenar os resultados das análises
total_consumo = 0
dias_cumpriram_meta = 0  # Contador de dias que cumpriram ou superaram a meta
meta = 150  # Meta de consumo sustentável em kWh

# Inicialização de valores para o maior e menor consumo
maior_consumo = None
menor_consumo = None

# Loop para entrada e processamento dos dados de consumo diário
for i in range(1, n + 1):
    consumo = int(input(f"Insira o consumo de energia no dia {i} (em kWh): "))

    # Atualiza o consumo total
    total_consumo += consumo

    # Verifica se o consumo atinge ou supera a meta
    if consumo <= meta:
        dias_cumpriram_meta += 1

    # Identifica o maior e o menor consumo
    if maior_consumo is None or consumo > maior_consumo:
        maior_consumo = consumo
    if menor_consumo is None or consumo < menor_consumo:
        menor_consumo = consumo

# Cálculo da média de consumo
media_consumo = total_consumo / n

# Contagem de dias que não cumpriram a meta
dias_nao_cumpriram_meta = n - dias_cumpriram_meta

# Relatório de Resultados
print("\n--- Relatório de Consumo de Energia ---")
if dias_cumpriram_meta == n:
    print("Parabéns! Todos os dias cumpriram a meta de consumo sustentável.")
elif dias_cumpriram_meta == 0:
    print("Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.")
else:
    print(f"{dias_cumpriram_meta} dias cumpriram a meta e {dias_nao_cumpriram_meta} dias não cumpriram a meta.")
print(
    f"A média de consumo foi de {media_consumo:.2f} kWh. O maior consumo foi de {maior_consumo} kWh e o menor consumo foi de {menor_consumo} kWh.")

print('Obrigado pelas informações e por participar!')
