def converter_valor(valor_str):
    #Substituindo vírgulas por pontos e retirando espaço em branco
    valor_str = valor_str.replace(',', '.').replace(' ', '')
    try:
        return float(valor_str)  #Tenta converter para float
    except ValueError:
        print("Formato inválido. Use um número válido.")
        return None

print("### Gerador de Preço SHIBA INU ###")

while True:
    capitalizacao_str = input('Qual o valor da capitalização em bilhões? ')
    capitalizacao = converter_valor(capitalizacao_str)

    supply_str = input('Qual o supply em questão em trilhões? ')
    supply = converter_valor(supply_str)

    if capitalizacao is not None and supply is not None:
        capitalizacao *= 10 * 1e9  # Multiplica a capitalização por 10 e converte para unidades
        supply *= 1e12 
        break

while True:
    queima_mensal_str = input('Qual a média de queima por mês? ')
    queima_mensal = converter_valor(queima_mensal_str)

    if queima_mensal is not None:
        break

while True:
    anos_futuros_str = input('Para quantos anos daqui a frente você deseja supor o preço? ')
    anos_futuros = converter_valor(anos_futuros_str)

    if anos_futuros is not None:
        break 

queima_anual = queima_mensal * 12
preco_hoje = capitalizacao / supply

for i in range(1, int(anos_futuros) + 1):
    supply -= queima_anual
    preco = capitalizacao / supply
    print(f'O valor do ativo no ano {i} será de: {preco:.8f}')
