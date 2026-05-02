qtd_pessoas = int(input("Escreva a quantidade de pessoas que vão dividir a conta: "))
valor_conta = float(input("Escreva o valor total da conta: "))
valor_dividido = valor_conta / qtd_pessoas

print(f"Cada pessoa deve pagar R$ {valor_dividido:.2f}.")