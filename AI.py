# Librerias necesarias
import random

# Definir constantes que nos serviran
INF = float('inf')

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
        self.own_turn = -1
        self.enemy_turn = -1
        self.white_space = 0

    # Metodos publicos
    def best_move(self, board : list, num_turn : int, depth = 5) -> int:
        # Instanciar valores en los atributos
        self.board = board
        self.own_turn = 1 if (num_turn == 1) else 2
        self.enemy_turn = 1 if(self.own_turn != 1) else 2

        # Tomar en cuenta otros aspectos
        best_score = -INF
        best_move_finded = None
        alpha = -INF
        beta = INF

        # Vamos a generar todos los movimientos y se procedera a analizarlos
        

        # retornara un numero entre 0-6        
        return random.randint(0, 6) # ! Claro que no dejare esto jaja
    
    # Metodos privados
    def __minimax(self, depth, alpha, beta, max_player):
        if depth == 0:
            return

        # Get Max(NUM_PLAYER)
        if max_player:
            max_value = -INF

            return max_value
        
        # Get Min(NUM_RIVAL)
        min_value = -INF
        return min_value
    
    def __value(self, s):
        # if s is terminal: return U(s)
        if s is max: return self.__max_value(s)        
        if s is min: return self.__min_value(s)
        
        return None
    
    def __max_value(self, s):
        m = -INF
        # for s2 in successors(s):
        #     m = max(m, self.__value(s2))
        return m
    
    def __min_value(self, s):
        m = -INF
        # for s2 in successors(s):
        #     m = min(m, self.__value(s2))
        return m
    
    def __value(self, depth, a, b):
        # a: mejor valor de MAX
        # b: mejor valor de MIN

        # if cutoff(s, depth): return h(s)
        # if s is terminal: return U(s)
        # if s is max: return self.__max_value(s, depth, a, b)
        # if s is min: return self.__min_value(s, depth, a, b)

        return None
    
    def __max_value(self, s, depth, a, b):
        v = -INF
        # for s2 in successors(s):
        #     v = max(v, self.__value(s2, depth + 1, a, b))
        #     if v > b: return v
        #     a = max(a, v)
        return v

    def __min_value(self, s, depth, a, b):
        v = -INF
        # for s2 in successors(s):
        #     v = min(v, self.__value(s2, depth + 1, a, b))
        #     if v > b: return v
        #     a = min(a, v)
        return v