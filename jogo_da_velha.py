from random import randint
class JogoDaVelha:
    def __init__(self):
        """Inicializa o tabuleiro e define os jogadores."""
        self._tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self._jogador_1 = 'X'
        self._jogador_2 = 'O'
        self._jogador_atual = self._jogador_1

    def apresentar_tabuleiro(self):
        """Exibe o tabuleiro para o usuário na linha de comando."""
        print('tabuleiro atual')
        for item in self._tabuleiro:
            print(item)

    def jogar(self, linha, coluna, jogador):
        """Marca a posição no tabuleiro com o símbolo do jogador.
        Args:
            linha (int): A linha onde o jogador quer jogar.
            coluna (int): A coluna onde o jogador quer jogar.
            jogador (str): O símbolo do jogador ('X' ou 'O').
        """
        self._tabuleiro[linha][coluna] = jogador

    def validar_jogada(self, linha, coluna):
        """Verifica se a jogada é válida (a posição está vazia).
        Args:
            linha (int): A linha da jogada.
            coluna (int): A coluna da jogada.
        Returns:
            bool: True se a posição não está ocupada, False caso contrário.
        """
        if self._tabuleiro[linha][coluna] == ' ':
            return True
        return False

    def verificar_empate(self):
        """Verifica se o jogo terminou em empate.
        Returns:
            bool: True se todas as posições estão ocupadas e não há vencedor, False caso contrário.
        """
        for linha in self._tabuleiro:
            for item in linha:
                if item == ' ':
                    return False
        return True

    def verificar_vitoria(self):
        """Verifica se há um vencedor.
        Returns:
            bool: True se há um vencedor, False caso contrário.
        """
        # verificar linhas
        for i in range(3):
            if self._tabuleiro[i][0] == self._tabuleiro[i][1] == self._tabuleiro[i][2] != ' ':
                return True
        # verificar colunas
        for i in range(3):
            if self._tabuleiro[0][i] == self._tabuleiro[1][i] == self._tabuleiro[2][i] != ' ':
                return True
        # verificar diagonais
        if self._tabuleiro[0][0] == self._tabuleiro[1][1] == self._tabuleiro[2][2] != ' ':
            return True
        if self._tabuleiro[0][2] == self._tabuleiro[1][1] == self._tabuleiro[2][0] != ' ':
            return True
        return False

    def jogador_atual(self):
        """Retorna o jogador atual.
        Returns:
            str: O símbolo do jogador atual ('X' ou 'O').
        """
        return self._jogador_atual

    def alternar_jogador(self):
        """Alterna o jogador atual."""
        if self._jogador_atual == self._jogador_1:
            self._jogador_atual = self._jogador_2
        else:
            self._jogador_atual = self._jogador_1

    def jogar_posicao_aleatoria(self):
        """Faz uma jogada em uma posição aleatória."""
        linha = randint(0, 2)
        coluna = randint(0, 2)
        if self.validar_jogada(linha, coluna):
            return linha, coluna
        else:
            self.jogar_posicao_aleatoria()

    def verificar_vitoria_futura(self, jogador):
        """Verifica se o jogador pode vencer na próxima jogada.
        Args:
            jogador (str): O símbolo do jogador ('X' ou 'O').
        Returns:
            tuple: A posição (linha, coluna) onde o jogador pode vencer, ou None se não houver tal posição.
        """
        # verificar linhas
        for i in range(3):
            if self._tabuleiro[i][0] == self._tabuleiro[i][1] == jogador and self._tabuleiro[i][2] == ' ':
                return i, 2
            if self._tabuleiro[i][0] == self._tabuleiro[i][2] == jogador and self._tabuleiro[i][1] == ' ':
                return i, 1
            if self._tabuleiro[i][1] == self._tabuleiro[i][2] == jogador and self._tabuleiro[i][0] == ' ':
                return i, 0
        # verificar colunas
        for i in range(3):
            if self._tabuleiro[0][i] == self._tabuleiro[1][i] == jogador and self._tabuleiro[2][i] == ' ':
                return 2, i
            if self._tabuleiro[0][i] == self._tabuleiro[2][i] == jogador and self._tabuleiro[1][i] == ' ':
                return 1, i
            if self._tabuleiro[1][i] == self._tabuleiro[2][i] == jogador and self._tabuleiro[0][i] == ' ':
                return 0, i
        # verificar diagonais
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
