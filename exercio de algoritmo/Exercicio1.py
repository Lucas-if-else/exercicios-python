"""
n=float(input("Digite número: "))
rels: float = n % 2
if rels == 0:
    print("O número é par")
else:    print("O número é impar")
"""
#2
""""
n1= float(input("Digite o primeiro número: "))
n2= float(input("Digite o segundo número: "))
if n1 > n2:
    print(f"O número {n1} é maior que o número {n2}")
elif n2 > n1:
    print(f"O número {n2} é maior que o número {n1}")
else:
    print(f"Os números {n1} e {n2} são iguais")
"""
#3
"""""
while True:
    n = float(input("Digite um número: "))
    if n > 0:
        print("O número é positivo")
        break
    elif n < 0:
        print("O número é negativo")
    else:
        print("O número é zero")
"""
#4
"""""
print("1-Bom dia!")
print("2-Tchau!")
print("3-Sair!")
while True:    
    palavra = input("Digite uma palavra: ")
    if palavra == "1":
        print("Bom dia!")
    elif palavra == "2":
        print("Tchau!")
    elif palavra == "3":
        print("Ate mais!")
        break
    else:
        print("Opção invalida, tente novamente")
"""
#5
"""
numeros = []
for num in range(5):
     numero = float(input(f"Digite o {num+1}º número: "))
     numeros.append(numero)
     soma = sum(numeros)
print(f"A soma dos números é: {soma}")
"""
#6
"""
contador = []
resultado = 0
negativo = 0
for num in range(5):
    numero = float(input(f"Digite o {num+1}º número: "))
    contador.append(numero)
    if numero > 0:
        resultado = resultado+1
    else:
        negativo = negativo+1
print(f"A quantidade de números positivos é: {resultado}")
print(f"A quantidade de números negativos é: {negativo}")
"""

#7
mediq = []
while True:
        for nota in range(3):
            notaq = float(input(f"Digite a {nota+1}ª nota: "))
            mediq.append(notaq)
            if notaq < 0 or notaq > 10 :
                print("Nota invalida, informe novamente")
                break
            else:
             media = sum(mediq) / len(mediq)
            
        print(f"A média das notas é: {media}")
        