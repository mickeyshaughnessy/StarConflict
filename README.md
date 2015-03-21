Star Conflict API and client design 
-------------
Initial client is run on the command line.
Players take turns performing actions - after 
each action the state of the game is updated 
on the remote server and the new game state is
displayed through the client.

The game state is represented as a JSON 'game' object according to
the following scheme:

```
models = {
        'game' : {
            '_id': basestring,
        ...
        },
    ...
    }
```

A game object contains many fields:
``` 
game._id
player1
player2
p1_board
p1_hand
p1_deck
p1_discard
p2_board
p2_hand
p2_deck
p2_discard
```

After each player action, the game state is updated on the server
and pushed to the clients. Clients will re-render the game state
whenever it is pushed to them from the remote server or after a local
player action.

The entire Star Conflict platform consists of a single game server interacting with
clients and updating game state according to rules. 

Command Line Client
-------

Future versions will include Android client, iOS client, 
and OSX versions. 

Users interact with the game by typing commands.

Game Server
-------------
At the core of the game server is an update function, `U`, that takes a game
object, `g`, and an `event` and generates a new game state, `g'`. 

```
g' = U(g,event)
```

Candidate events are first validated to determine if they are valid according
to the game rules and current game state. A later version of the game will have
the validator functionality on the game clients, so only valid events are sent 
to the server.

Valid events are then processed, triggering various functions that modify the
game state. A final game state is then stored in Redis, pushed to the client,
and the program waits for the next event.

-------

As an example, player1 on his turn may submit a request to attack player2. 
This means he wants to apply his current attack total to decrease player2's 
prestige. The event `attack player2` and the game state `g` are validated -
`if g.active = p1 and len(x for x in g.board.p2 if x.is_blocker == True)` 

