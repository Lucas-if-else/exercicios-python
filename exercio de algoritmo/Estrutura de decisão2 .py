while True:
    notas = []
    for i in range(5):
        nota = input(f"informe a {i+1}ª nota: ").upper()
        notas.append(nota)
    if all(nota in "ABCDE" for nota in notas):
        break
    else:
        print("Nota invalida, informe novamente")
valor = {"A": 10, "B": 7, "C": 5, "D": 3, "E": 0 }
media = sum(valor[nota] for nota in notas) / len(notas)
if media >=6:
    print("Voce estar aprovado!!!!")
elif media>=4: 
    print("Voce estar de recuperação")
else:
    print("Voce Estar Reprovado")
    