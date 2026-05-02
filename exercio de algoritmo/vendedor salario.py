nome = input("Escreva o nome do vendedor: ")
sal_fix = float(input("Escreva o valor do salário fixo do vendedor: "))
total_vendas = float(input("Escreva o valor total das vendas do vendedor: "))
if total_vendas <= 5000:
    comissao = (total_vendas * 0.10)
elif total_vendas > 5000 and total_vendas <= 15000:
    comissao = (total_vendas * 0.12)
else:
    comissao = (total_vendas * 0.15)
sal_total = sal_fix + comissao
print(f"O salário total do vendedor {nome} é de R$ {sal_total:.2f} sua comissão é de R$ {comissao:.2f}.")