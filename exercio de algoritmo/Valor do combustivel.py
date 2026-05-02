valor_litro = float(input("informe o valor do litro do combustivel: "))
valor_pago = float(input("informe o valor pago pelo combustivel: "))
litros_comprados = valor_pago / valor_litro
print(f"Voce comprou {litros_comprados:.2f} litros de combustivel.")