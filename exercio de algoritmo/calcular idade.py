nome = input("Informe seu nome: ")
ano_nascimento = int(input("Informe seu ano de nascimento: "))
mes_nascimento = int(input("Informe seu mês de nascimento: "))
dia_nascimento = int(input("Informe seu dia de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade = ano_atual - ano_nascimento
mes = mes_nascimento
dia = dia_nascimento
print(f"{nome}, você tem {idade} anos, nasceu no dia {dia} do mês {mes}.")