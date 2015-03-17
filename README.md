Star Conflict API and client design 
-------------
Initial client is run on the command line.
Players take turns performing actions - after 
each action the state of the game is updated 
on the remote server and the new game state is
displayed through the client.

The game state is represented as a json 'game' object according to
the following scheme:

```json
models = {
    'game' : {
        Required('_id'): basestring,
        ...
    },
    ...
}
```

A game object contains the following fields:
``` 
game._id
player1_id
player2_id
p1_board
p1_hand
p1_deck
p1_discard
p2_board
p2_hand
p2_deck
p2_discard
stats
```

After each player action, the game state is updated on the server
and pushed to the clients. Clients will re-render the game state
whenever it is pushed to them from the remote server or after a local
player action.

The entire Star Conflict consists of a single game database interacting with
clients and updating game state according to rules. 










Future versions will include Android client, iOS client, 
and OSX versions. 

Users interact with the program by typing commands.


