# Librerias necesarias
import random

# Definir constantes que nos serviran
INF = float('inf')
COLS = 7
ROWS = 6
SCORE_WINNER = 10
ONE = 4
TWO = 2
THREE = 5

'''
TOMAR EN CUENTA LO SIGUIENTE:
-> min-max
-> alpha/beta
-> heuristica/heuristic h(n)
'''

class PowerfullAI(object):
    # Constructor
    def __init__(self) -> None:
        self.board = []
        self.player_turn = -1
        self.enemy_turn = -1
        self.white_space = 0

    # Metodos publicos
    def best_move(self, board : list, num_turn : int, depth = 6) -> int:
        # Instanciar valores en los atributos
        self.board = board
        self.player_turn = 1 if (num_turn == 1) else 2
        self.enemy_turn = 1 if(self.player_turn != 1) else 2

        # Tomar en cuenta otros aspectos
        board_copy = [row.copy() for row in self.board]
        alpha = -INF
        beta = INF

        # Vamos a generar todos los movimientos y se procedera a analizarlos
        move, _ = self.__minimax(board_copy, depth, alpha, beta, True, self.player_turn)

        # retornara un numero entre 0-6        
        return move
    
    # Metodos privados
    def __minimax(self, board, depth, alpha, beta, max_player, player) -> int:
        moves = [i for i in range(COLS) if board[0][i] == 0]
        
        if depth == 0 or not moves: 
            return (None, self.__heuristic_eval(player))

        if max_player:
            max_score = -INF
            best_move = None

            for move in moves:
                temp_board = self.new_board(board, move, player)
                _, new_score = self.__minimax(temp_board, depth - 1, alpha, beta, False, self.player_turn)

                if new_score > max_score:
                    max_score = new_score
                    best_move = move

                alpha = max(alpha, max_score)
                if alpha >= beta:
                    break

            return (best_move, max_score)
        else:  # Minimizing player
            min_score = INF
            best_move = None

            for move in moves:
                temp_board = self.new_board(board, move, 2 if self.player_turn == 1 else 1)
                _, new_score = self.__minimax(temp_board, depth - 1, alpha, beta, True, self.player_turn)

                if new_score < min_score:
                    min_score = new_score
                    best_move = move

                beta = min(beta, min_score)
                if alpha >= beta:
                    break

            return (best_move, min_score)
        
    def new_board(self, board, column_index, player):
        create = [row.copy() for row in board]

        for row in range(ROWS - 1, -1, -1):
            if create[row][column_index] == 0:
                create[row][column_index] = player
                break

        return create
    
    def __heuristic_eval(self, player):
        oponent = 1 if player == 2 else 2
        score = 0

        for row in range(ROWS):
            for col in range(COLS - 3):
                window = [self.board[row][col], self.board[row][col+1], self.board[row][col+2], self.board[row][col+3]]
                score += self.__evaluate_window(window, player, oponent)

        for row in range(ROWS - 3):
            for col in range(COLS):
                window = [self.board[row][col], self.board[row+1][col], self.board[row+2][col], self.board[row+3][col]]
                score += self.__evaluate_window(window, player, oponent)

        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                window = [self.board[row][col], self.board[row+1][col+1], self.board[row+2][col+2], self.board[row+3][col+3]]
                score += self.__evaluate_window(window, player, oponent)

        for row in range(3, ROWS):
            for col in range(COLS - 3):
                window = [self.board[row][col], self.board[row-1][col+1], self.board[row-2][col+2], self.board[row-3][col+3]]
                score += self.__evaluate_window(window, player, oponent)

        return score
    
    def __evaluate_window(self, window, player, oponent):
        score = 0

        if window.count(player) == 4:
            score += SCORE_WINNER
        elif window.count(player) == 3 and window.count(0) == 1:
            score += THREE
        elif window.count(player) == 2 and window.count(0) == 2:
            score += TWO
        elif window.count(oponent) == 3 and window.count(0) == 1:
            score -= ONE

        return score
    