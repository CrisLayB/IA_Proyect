# python3 client.py CristianPy 192.168.1.131 4000 142857

from AI import PowerfullAI
from socketIO_client import SocketIO
import random
import sys

# Solicitar argumentos
if len(sys.argv) != 5:
    print("Invalid Args")
    quit()

# Imprimir bien los valores
user_name = sys.argv[1]
server_url = "http://" + sys.argv[2]
server_port = sys.argv[3]
id_tournament = int(sys.argv[4])

# Crear socket para conectarse
socketIO = SocketIO(server_url, server_port)

# Llamar a la IA
ai = PowerfullAI()

def on_connect():
    print("Connected to server")
    socketIO.emit('signin', {
        'user_name': user_name,
        'tournament_id': id_tournament,
        'user_role': 'player'
    })

def on_ok_signin():
    print("Successfully signed in!")

def on_ready(data):
    game_id = data['game_id']
    player_turn_id = data['player_turn_id']
    board = data['board']
    
    print("=============================")
    print(data)
    print("=============================")
    print(board)
    print("=============================")
    # TODO: Your logic / user input here
    # Mejor movimiento # Matriz : 7 * 6
    move = ai.best_move(board, player_turn_id)

    print("Move in:", move)
    socketIO.emit('play', {
        'tournament_id': id_tournament,
        'player_turn_id': player_turn_id,
        'game_id': game_id,
        'movement': move
    })


def on_finish(data):
    game_id = data['game_id']
    player_turn_id = data['player_turn_id']
    winner_turn_id = data['winner_turn_id']
    board = data['board']
    
    # Your cleaning board logic here
    
    print("Winner:", winner_turn_id)
    print(board)

    socketIO.emit('player_ready', {
        'tournament_id': id_tournament,
        'player_turn_id': player_turn_id,
        'game_id': game_id
    })

socketIO.on('connect', on_connect)
socketIO.on('ok_signin', on_ok_signin)
socketIO.on('ready', on_ready)
socketIO.on('finish', on_finish)

socketIO.wait()