INF = float('inf')

class PowerfullAI(object):
    # Constructor
    def __init__(self) -> None:
        ...

    # Metodos publicos
    def best_move(self, board : list) -> int:
        return
    
    # Metodos privados
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