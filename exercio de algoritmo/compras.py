nomepdt = input("Digite o nome do produto: ")
preco_unit = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
total = preco_unit * quantidade
print(f"O total a pagar pelo produto {nomepdt} é: R${total:.2f}")

