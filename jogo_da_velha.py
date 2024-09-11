class JogoDaVelha:
    def __init__(self):
        self._tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self._jogador_1 = 'X'
        self._jogador_2 = 'O'
        self._jogador_atual = self._jogador_1

    def apresentar_tabuleiro(self):
        return self._tabuleiro

    def jogador_atual(self):
        return self._jogador_atual

    def alternar_jogador(self):
        if self._jogador_atual == self._jogador_1:
            self._jogador_atual = self._jogador_2
        else:
            self._jogador_atual = self._jogador_1

    def jogar(self, linha, coluna, jogador):
        self._tabuleiro[linha][coluna] = jogador

    def validar_jogada(self, linha, coluna):
        if self._tabuleiro[linha][coluna] == ' ':
            return True
        return False

    def verificar_vitoria(self):
        for i in range(3):
            if self._tabuleiro[i][0] == self._tabuleiro[i][1] == self._tabuleiro[i][2] != ' ':
                return True
            if self._tabuleiro[0][i] == self._tabuleiro[1][i] == self._tabuleiro[2][i] != ' ':
                return True
        if self._tabuleiro[0][0] == self._tabuleiro[1][1] == self._tabuleiro[2][2] != ' ':
            return True
        if self._tabuleiro[0][2] == self._tabuleiro[1][1] == self._tabuleiro[2][0] != ' ':
            return True
        return False

    def verificar_empate(self):
        for linha in self._tabuleiro:
            for item in linha:
                if item == ' ':
                    return False
        return True

    def mapear_tecla(self, tecla):
        if tecla == '7':
            return 0, 0
        if tecla == '8':
            return 0, 1
        if tecla == '9':
            return 0, 2
        if tecla == '4':
            return 1, 0
        if tecla == '5':
            return 1, 1
        if tecla == '6':
            return 1, 2
        if tecla == '1':
            return 2, 0
        if tecla == '2':
            return 2, 1
        if tecla == '3':
            return 2, 2
        return None
