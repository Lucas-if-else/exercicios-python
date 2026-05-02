cadastro : str = input("Deseja cadastrar um novo usuário? (S/N): ").upper()
    if cadastro == "S":
        nome : str = input("Digite o nome do usuário: ")
        senha : str = input("Digite a senha do usuário: ")
        print(f"Usuário {nome} cadastrado com sucesso!")
    elif cadastro == "N":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
    Saldo = 1000
    while True:
        print("\n=== CAIXA ELETRÔNICO ===")
        print("1 - Consultar saldo")
        print("2 - Sacar dinheiro")
        print("3 - Depositar dinheiro")
        print("4 - Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Seu saldo é: R${Saldo:.2f}")

        elif escolha == "2":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque <= Saldo:
                Saldo -= valor_saque
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar o saque.")

        elif escolha == "3":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            Saldo += valor_deposito
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")

        elif escolha == "4":
            print("Saindo do caixa eletrônico. Tenha um bom dia!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")