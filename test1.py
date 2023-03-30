print("### Gerador de Preço SHIBA INU ###")
capitalizacao = int(input('Qual o valor da capitalização em bilhões? '))
supply = int(input('Qual o supply em questão em trilhões? '))

capitalizacao *= 1000000000
supply *= 1000000000000

queima_mensal = int(input('Qual a média de queima por mês? '))
anos_futuros = int(input('Para quantos anos daqui a frente você deseja supor o preço? '))

queima_anual = queima_mensal * 12
preco_hoje = capitalizacao / supply

for i in range(1, anos_futuros+1):
    supply -= queima_anual
    preco = capitalizacao / supply
    print(f'O valor do ativo no ano {i} será de: {preco:.6f}')
