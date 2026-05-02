import random
vida_jogador = 200
Defesa_jogador = random.uniform(1.67,15.32)
vida_inimigo = 15
print("Bem-vindo ao jogo de texto!")
print("Você é um aventureiro corajoso enfrentando um inimigo feroz.")
print("Prepare-se para a batalha!")
while True:
    print("\n=== BATALHA ===")
    print(f"Sua vida: {vida_jogador}")
    print(f"Vida do inimigo: {vida_inimigo}")
    print(f"Sua defesa: {Defesa_jogador}")
    print("\n1 - Atacar")
    print("2 - Defender")
    print("3 - Fugir")
    
    escolha = input("Escolha: ")

    if escolha == "1":
        dano = 5
        vida_inimigo -= dano
        print(f"Você atacou e causou {dano} de dano!")

    elif escolha == "2":
        print("Você se defendeu! Dano reduzido.")
        dano = 2
        vida_jogador -= dano

    elif escolha == "3":
        print("Você fugiu da batalha!")
        break

    else:
        print("Opção inválida!")
        continue

    # turno do inimigo
    if vida_inimigo > 0:
        dano_inimigo = 4
        vida_jogador -= dano_inimigo
        print(f"O inimigo te atacou e causou {dano_inimigo} de dano!")

    # verificar fim do jogo
    if vida_jogador <= 0:
        print("💀 Você morreu! Fim de jogo.")
        break

    if vida_inimigo <= 0:
        print("🏆 Você venceu o inimigo!")
        break