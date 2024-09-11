from jogo_da_velha_rl import JogoDaVelhaRL


def main():
    """Função principal que executa o jogo da velha."""
    jogo = JogoDaVelhaRL()

    print('\nINICIO DO JOGO DA VELHA\n')
    for item in jogo.apresentar_tabuleiro():
        print(item)

    while(True):
        jogador = jogo.jogador_atual()

        if jogador == 'X':
            tecla = input(f'\nJogador {jogador} Digite a posição (1-9): ')
            linha, coluna = jogo.mapear_tecla(tecla)
        else:
            linha, coluna = (jogo.jogar_no_centro() or
                             jogo.verificar_vitoria_futura('O') or
                             jogo.verificar_vitoria_futura('X') or
                             jogo.jogar_nas_pontas() or
                             jogo.jogar_posicao_aleatoria())

        if jogo.validar_jogada(linha, coluna):
            jogo.jogar(linha, coluna, jogo.jogador_atual())
        else:
            print('Jogada inválida. Escolha uma posição vazia.')
            continue

        print(f'\nTabuleiro após o jogador {jogador} escolher a posição\n')
        for item in jogo.apresentar_tabuleiro():
            print(item)

        jogo.salvar_tabuleiro()

        if jogo.verificar_vitoria():
            print(f'\nVITÓRIA DO JOGADOR {jogo.jogador_atual()}')
            break

        if jogo.verificar_empate():
            print('\nEMPATE\n')
            break

        jogo.alternar_jogador()


if __name__ == '__main__':
    main()
