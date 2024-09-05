from jogo_da_velha import JogoDaVelha


def main():
    """Função principal que executa o jogo da velha."""
    jogo_da_velha = JogoDaVelha()

    while(True):
        jogo_da_velha.apresentar_tabuleiro()

        if jogo_da_velha.jogador_atual() == 'X':
            linha = int(input('Digite a linha (0, 1, 2): '))
            coluna = int(input('Digite a coluna (0, 1, 2): '))
        else:
            linha, coluna = jogo_da_velha.jogar_posicao_aleatoria()

        if jogo_da_velha.validar_jogada(linha, coluna):
            jogo_da_velha.jogar(linha, coluna, jogo_da_velha.jogador_atual())
        else:
            print('Jogada inválida. Escolha uma posição vazia.')
            continue

        if jogo_da_velha.verificar_vitoria():
            print(f'Vitória {jogo_da_velha.jogador_atual()}')
            break

        if jogo_da_velha.verificar_empate():
            print('Empate')
            break

        jogo_da_velha.alternar_jogador()

    jogo_da_velha.apresentar_tabuleiro()
    print('Fim de jogo')


if __name__ == '__main__':
    main()
