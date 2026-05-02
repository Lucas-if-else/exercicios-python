dolar = float(input("Digite a cotação do dólar: ").replace(",", "."))
real = float(input("Digite a quantidade em reais: "))
conversao = real / dolar
print(f"O valor em dólares é: ${conversao:.2f}")