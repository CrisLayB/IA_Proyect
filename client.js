// * Pruebas de forma local
// node client.js Cristian

// * Para el servidor de la clase:
// node client.js Cristian 192.168.1.134 4000 142857

var args = process.argv.slice(2);
console.log(args)

if(args.length != 4){
    console.log("Insufficient Args, Example:")
    console.log("node client.js userName ip port tournamentId")
    return
}

const name = args[0]
const ip = args[1]
const port = args[2]
const idTournament = parseInt(args[3])

const io = require('socket.io-client');
const socket = io('http://' + ip + ":" + port);

socket.on('connect', function(){
    console.log("Conected to the server");
    socket.emit('signin', {
        user_name: name,
        tournament_id: idTournament,
        user_role: 'player'
    });
});

socket.on('ok_signin', function(){
    console.log("Successfully signed in!");
});

socket.on('ready', function(data){
    var gameID = data.game_id;
    var playerTurnID = data.player_turn_id;
    var board = data.board;
    
    // TODO: Your logic / user input here
    // Mejor movimiento // Matriz : 7 * 6
    
    socket.emit('play', {
        tournament_id: idTournament,
        player_turn_id: playerTurnID,
        game_id: gameID,
        movement: Math.floor(Math.random() * 7)
    });
});

socket.on('finish', function(data){
    var gameID = data.game_id;
    var playerTurnID = data.player_turn_id;
    var winnerTurnID = data.winner_turn_id;
    var board = data.board;
    
    // TODO: Your cleaning board logic here
    // ...
    
    socket.emit('player_ready', {
        tournament_id: idTournament,
        player_turn_id: playerTurnID,
        game_id: gameID
    });
});

socket.on('disconnect', function(){
        console.log("Server Disconected");
    }
);