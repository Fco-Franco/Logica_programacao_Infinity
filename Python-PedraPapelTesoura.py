#region
# Neste projeto você desenvolverá o jogo pedra, papel e tesoura. Os jogadores serão o usuário e o computador. O jogo deve iniciar pedindo ao usuário para escolher entre "pedra", "papel" ou "tesoura" e então o computador irá fazer a escolha aleatoriamente, após isso, o jogo deve informar quem venceu. Para recordar: 
# Pedra > tesoura
# Tesoura > Papel
# Papel > Pedra
# Utilize funções para separar cada funcionalidade do jogo! Dica : Utilize a função random.choice(lista) do pacote andom para realizar a escolha do computador.

import random
qtde_empate =0
qtde_jogador1=0
qtde_jogador2=0

lista_pedra_papel_tesoura = ["pedra", "papel", "tesoura"]

def pedraPapelTesoura(jogador1,jogador2):
    if jogador1 == jogador2:
        return  "Empate"
    if (jogador1 == "pedra" and jogador2=="tesoura") or (jogador1 == "tesoura" and jogador2=="papel") or (jogador1 == "papel" and jogador2=="pedra"):
        return  "Voce"
    else:
        return  "Máquina"

while True:
    jogador1 = str(input("Escolha pedra, papel, tesoura: ")).lower()
    if jogador1 not in lista_pedra_papel_tesoura:
        print ("Só é permitido digitar pedra, papel, tesoura")
    else:
        print(f"Jogador 1(Voce) jogou: {jogador1}")
        jogador2 = random.choice(lista_pedra_papel_tesoura)
        print(f"Jogador 2(Máquina) jogou: {jogador2}")
        if pedraPapelTesoura(jogador1,jogador2)== "Empate":
            print(f"Deu empate")
            qtde_empate += 1
        else:
            print(f"{pedraPapelTesoura(jogador1,jogador2)} ganhou")
            if pedraPapelTesoura(jogador1,jogador2)== "Voce":
                qtde_jogador1 += 1
            else:
                qtde_jogador2 += 1
        jogar_novamente=input("\nDeseja jogar novamente? Digite n para sair, ou qualquer tecla para continuar: ").lower()
        if jogar_novamente == "n":
            print(f"""\nForam {qtde_jogador2+qtde_jogador1+qtde_empate} partidas. 
        Placar:
            {qtde_empate} empates; 
            Jogador 1(Voce) ganhou {qtde_jogador1} vezes; 
            Jogador 2(Máquina) ganhou {qtde_jogador2} vezes;\n""")
            break

#endregion
