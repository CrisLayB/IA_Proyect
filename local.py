from AI import PowerfullAI
import random

EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

board = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
]

def edit_board(num : int, type_player : int) -> None:
    # Eximar desde la ultima fila hasta el principio
    count = len(board) - 1
    while count >= 0:
        if(board[count][num] == EMPTY):
            if type_player == 1:
                board[count][num] = PLAYER1
                return True
            if type_player == 2:
                board[count][num] = PLAYER2
                return True
        count -= 1
    
    return False

def check_4_circles_is_connected():
    # Revisar horizontalmente
    for row in range(6):
        for col in range(4):
            if (
                board[row][col]
                and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]
            ):
                return board[row][col]

    # revisar verticalmente
    for row in range(3):
        for col in range(7):
            if (
                board[row][col]
                and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]
            ):
                return board[row][col]

    # Revisar diagonalidad (pendiente positiva)
    for row in range(3):
        for col in range(4):
            if (
                board[row][col]
                and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]
            ):
                return board[row][col]

    # Revisar diagonalidad (pendiente negativa)
    for row in range(3):
        for col in range(3, 7):
            if (
                board[row][col]
                and board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3]
            ):
                return board[row][col]
    
    return None # Cuando todavia no hay ganador

def game_print():
    print("\n")
    for table in board:
        print(table)
    print("\n")

ai = PowerfullAI()
player_turn = random.randint(1, 2)
finish = False

while not finish:
    # Imprimir tabla de allconnect-4
    game_print()

    choice = -1

    # Turno de jugador
    if player_turn == 1:
        while choice < 0 or choice > 6:
            choice = int(input("PLAYER 1: Ingrese un numero (0-6): "))    
        edit_board(choice, 1)
        player_turn = 2
        winner = check_4_circles_is_connected()
        if winner != None:
            game_print()
            print(f"WINNER PLAYER #: {winner}\n")
            finish = True
        continue

    # Turno de IA
    if player_turn == 2:
        while choice < 0 or choice > 6:
            choice = int(input("PLAYER 2: Ingrese un numero (0-6): "))    
        edit_board(choice, 2)
        player_turn = 1
        winner = check_4_circles_is_connected()
        if winner != None:
            game_print()
            print(f"WINNER PLAYER #: {winner}\n")
            finish = True
        continue