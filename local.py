from AI import PowerfullAI
import random

EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

def define_empty_game():
    return [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    ]

def edit_board(board : list[list], num : int, type_player : int) -> None:
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
    
    print("\nIngresaste una columna que ya esta llena, porfavor ingresa otro\n")
    return False

def is_a_winner_ready(board : list[list]) -> int:
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

def is_draw(board : list[list]) -> bool:    
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def game_print(board : list[list]) -> None:
    print("\n")
    for table in board:
        print(table)
    print("\n")

def player_set(board : list[list], player_num : int) -> None:
    choice = -1
    while choice < 0 or choice > 6:
        choice = int(input(f"PLAYER {player_num}: Ingrese un numero (0-6): "))                
        if not edit_board(board, choice, player_num): choice = -1

def ia_set(board : list[list], player_num : int, ai_player : PowerfullAI) -> None:
    choice = -1
    while choice < 0 or choice > 6:
        choice = ai_player.best_move(board, player_num)
        if not edit_board(board, choice, player_num): choice = -1

ai = PowerfullAI()
player_turn = random.randint(1, 2)
finish = False
board = define_empty_game()

while not finish:
    # Imprimir tabla de allconnect-4
    game_print(board)

    # Revisar si ya hay un ganador
    winner = is_a_winner_ready(board)
    if winner != None:
        print(f"WINNER PLAYER #: {winner}\n")
        finish = True if input("¿Deseas seguir jugando? (s/n): ").lower() == "n" else False
        board = define_empty_game()
        continue

    # Revisar si es empate
    if is_draw(board):
        print(f"ESTO FUE UN EMPATE\n")
        finish = True if input("¿Deseas seguir jugando? (s/n): ").lower() == "n" else False
        board = define_empty_game()
        continue

    # Turno de Primer Jugador
    if player_turn == 1:
        player_set(board, 1) # ! Ingresar jugador con input
        # ia_set(board, 1, ai) # ? Poner IA a jugar contra nosotros
        player_turn = 2        
        continue

    # Turno de Segundo Jugador
    if player_turn == 2:
        # player_set(board, 2) # ! Ingresar jugador con input
        ia_set(board, 2, ai) # ? Poner IA a jugar contra nosotros
        player_turn = 1
        continue