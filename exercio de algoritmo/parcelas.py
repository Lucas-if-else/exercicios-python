valor = float(input("Informe o valor total a ser parcelado: "))
numero_parcelas = int(input("Informe o número de parcelas: "))
valor_parcela = valor / numero_parcelas
print(f"O valor de cada parcela será de R$ {valor_parcela:.2f}.")