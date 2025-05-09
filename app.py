import random

while True:

    rodadas_validas = 0
    pontos_jogador = 0
    pontos_computador = 0

    while rodadas_validas < 5:
        escolha = input("Escolha Pedra, Papel ou Tesoura: ").strip().capitalize()
        if escolha not in ["Pedra", "Papel", "Tesoura"]:
            print("Entrada inválida. Digite 'Pedra', 'Papel' ou 'Tesoura'.")
            continue

        rodadas_validas += 1
        computador = random.choice(["Pedra", "Papel", "Tesoura"])
        print(f"Computador escolheu: {computador}")

        if escolha == computador:
            print("Empate!")
        elif (escolha == "Pedra" and computador == "Tesoura") or \
             (escolha == "Papel" and computador == "Pedra") or \
             (escolha == "Tesoura" and computador == "Papel"):
            print("Jogador pontua!")
            pontos_jogador += 1
        else:
            print("Computador pontua!")
            pontos_computador += 1

        print(f"Placar: Jogador {pontos_jogador} x Computador {pontos_computador}\n")

    print("=== Resultado da série ===")
    print(f"Jogador: {pontos_jogador} | Computador: {pontos_computador}")
    if pontos_jogador > pontos_computador:
        print("Você venceu a série!")
    elif pontos_jogador < pontos_computador:
        print("Computador venceu a série!")
    else:
        print("A série terminou em empate!")
    print("=========================\n")

    resposta = input("Deseja jogar outra vez? (S/N): ").strip().upper()
    if resposta != "S":
        print("Obrigado por jogar!")
        break