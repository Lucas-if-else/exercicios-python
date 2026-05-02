from datetime import datetime
ano_nac= int(input("Escreva sseu ano de nacimento: "))
ano_atu= datetime.now().year
idade= ano_atu-ano_nac
if idade >=16 and idade >=70:
 print(f"voce tem {idade} anos voce pode votar")
elif idade >= 18:
 print(f"voce tem {idade} anos  voce é obrigado a votar")
else:
 print(f"voce tem {idade} anos voce nao pode votar")
 