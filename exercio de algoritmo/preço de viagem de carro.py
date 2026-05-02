Distacia = float(input("Digite a distância da viagem em km: "))
Consumo = float(input("Digite o consumo do carro em km/l: "))
preço_litro = float(input("Digite o preço do litro do combustível: "))
litros_necessarios = Distacia / Consumo
print(f"Serão necessários {litros_necessarios:.2f} litros de combustível para a viagem.")
print(f"O custo total da viagem será de R$ {litros_necessarios * preço_litro:.2f}.")