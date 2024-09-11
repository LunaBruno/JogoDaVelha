"""
Centro Primeiro:
    Sempre tente pegar a posição central se estiver disponível.
    Isso te dá o maior controle sobre o jogo.

Jogo nas Pontas:
    Se o centro estiver ocupado, tente pegar uma das pontas.
    As pontas são estratégicas porque podem fazer parte de várias linhas de vitória.

Bloqueie o Oponente:
    Sempre fique atento às possíveis jogadas de vitória do seu oponente e bloqueie-as.

Crie Duas Maneiras de Vencer:
    Tente criar uma situação em que você tenha duas jogadas de vitória possíveis.
    Isso força o oponente a bloquear uma, permitindo que você vença com a outra.

Bifurcação:
    Crie oportunidades onde você possa formar duas linhas de três possíveis (uma bifurcação).
    Isso torna difícil para o oponente bloquear ambas.

Cantos Opostos:
    Se o seu oponente pegar um canto, pegue o canto oposto.
    Isso pode te ajudar a preparar uma bifurcação.
"""
from random import randint
from jogo_da_velha import JogoDaVelha

class JogoDaVelhaRL(JogoDaVelha):
    def __init__(self):
        super().__init__()

    def reiniciar_tabuleiro(self):
        self._tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self._jogador_atual = self._jogador_1

    def posicoes_disponiveis(self):
        posicoes = []
        for i in range(3):
            for j in range(3):
                if self._tabuleiro[i][j] == ' ':
                    posicoes.append((i, j))
        return posicoes

    def jogar_posicao_aleatoria(self):
        posicoes = self.posicoes_disponiveis()
        return posicoes[randint(0, len(posicoes) - 1)]

    def verificar_vitoria_futura(self, jogador):
        for i in range(3):
            if self._tabuleiro[i][0] == self._tabuleiro[i][1] == jogador and self._tabuleiro[i][2] == ' ':
                return i, 2
            if self._tabuleiro[i][0] == self._tabuleiro[i][2] == jogador and self._tabuleiro[i][1] == ' ':
                return i, 1
            if self._tabuleiro[i][1] == self._tabuleiro[i][2] == jogador and self._tabuleiro[i][0] == ' ':
                return i, 0
        for i in range(3):
            if self._tabuleiro[0][i] == self._tabuleiro[1][i] == jogador and self._tabuleiro[2][i] == ' ':
                return 2, i
            if self._tabuleiro[0][i] == self._tabuleiro[2][i] == jogador and self._tabuleiro[1][i] == ' ':
                return 1, i
            if self._tabuleiro[1][i] == self._tabuleiro[2][i] == jogador and self._tabuleiro[0][i] == ' ':
                return 0, i
        if self._tabuleiro[0][0] == self._tabuleiro[1][1] == jogador and self._tabuleiro[2][2] == ' ':
            return 2, 2
        if self._tabuleiro[0][0] == self._tabuleiro[2][2] == jogador and self._tabuleiro[1][1] == ' ':
            return 1, 1
        if self._tabuleiro[1][1] == self._tabuleiro[2][2] == jogador and self._tabuleiro[0][0] == ' ':
            return 0, 0
        if self._tabuleiro[0][2] == self._tabuleiro[1][1] == jogador and self._tabuleiro[2][0] == ' ':
            return 2, 0
        if self._tabuleiro[0][2] == self._tabuleiro[2][0] == jogador and self._tabuleiro[1][1] == ' ':
            return 1, 1

    def salvar_tabuleiro(self):
        tabuleiro_em_linha = [item for linha in self._tabuleiro for item in linha]
        with open('tabuleiro.txt', 'a') as arquivo:
            arquivo.write(','.join(tabuleiro_em_linha) + '\n')

    def jogar_no_centro(self):
        if self._tabuleiro[1][1] == ' ':
            return 1, 1

    def jogar_nas_pontas(self):
        if self._tabuleiro[0][0] == ' ':
            return 0, 0
        if self._tabuleiro[0][2] == ' ':
            return 0, 2
        if self._tabuleiro[2][0] == ' ':
            return 2, 0
        if self._tabuleiro[2][2] == ' ':
            return 2, 2
