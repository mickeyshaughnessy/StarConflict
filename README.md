Star Conflict API and client design 
-------------
Initial client is run on the command line.
Players take turns performing actions - after 
each action the state of the game is updated 
on the remote server and the new game state is
displayed through the client.

To do:
--------
* Build client to:
  * communicate with server:
    * GET users and games.
    * POST to initiate games.
    * POST moves to games.
    * POST collection changes to users. 
  * Render games from JSON game, g.
  * Enable user to generate games, moves and collection changes.
* Add to Cards files:
  * Translate Google Sheets doc to card classes.
* Make server talk to client (API using Flask).
* Finalize core game functionality:
  * Start_game.
  * Instantiate Game from JSON game.
  * Validate events.
  * Update Game.
  * Check win condition.
  * Deinstantiate Game to JSON game.
* Flesh out data infrastructure:
  * Define SC_user objects.
  * Define methods for updating user collections.


Explantion of program structure:
-------------------------------

The game state is represented as a JSON game object as a part of the following 
schemata.

```
models = {
    'game' : {
        '_id': basestring,
        'pids': [basestring],
        'active': basestring,,
        'p1': {
            'hand': [basestring],
            'deck': [basestring],
            'board': [basestring],
            'discard': [basestring],
            'prestige': int,
            'population': int,
            'resource': int,
            'attack': int,
            'defense': int
        }
        'p2': {
            'hand': [basestring],
            'deck': [basestring],
            'board': [basestring],
            'discard': [basestring],
            'prestige': int,
            'population': int,
            'resource': int,
            'attack': int,
            'defense': int
        }

    },
    'user': {
        Required('_id'): basestring,
        Required('purchased'): [basestring],
        Required('user_name'): basestring,
        Required('win_loss_history'): [ basestring : basestring]
    }
}

```

The game objects are complete string representations of game states. These are
stored in the server Redis with keys `'game:'+<_id>` and are passed to clients.
When a change of state is initiated on the server:

1. Game states are instantiated from the game state representation, g, into a game, G - a group of Card and Player objects. 
2. The triggering event, `e`, is validated. 
3. The game G is modified by the triggering event and the Player and Card methods.
4. The final game state is deinstatiated into a new string representation, `g'`.


A player action on the client is pushed to the server
to update. After the update the new game state is pushed to the clients.
Clients will re-render the game state whenever it is pushed to them from the 
remote server or after a local player action.

The entire Star Conflict platform consists of a single game server interacting with
clients and updating game state according to rules.

Command Line Client
-------

Future versions will include Android client, iOS client, 
and OSX versions. 

Users interact with the command line client by typing commands.
The game state is represented by strings printed to stdout.

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

The update function instantiates the game -
creates a Card/Player representation (Game) for each card or player in the game.

Events are then processed, triggering various Card and Player methods that 
modify the Game. A new final game state (g') is then stored in Redis, pushed to 
the client, and the program waits for the next event.

-------
--------
As an example, player1 on his turn may submit a request to attack player2. 
This means he wants to apply his current attack total to decrease player2's 
prestige. 
The game state, `g`, is instantiated into a Game, `G`.
The combined event `e = attack p2` and the Game are validated:

```if G.active == 'p1' and 
len([x for x in G.p2['board'] if x.is_blocker == True]) == 0``` 

For an attack event request, the validator checks that the requesting player
is active and that the opposing player has no blockers in play. 

Given the validated event, `attack p2`, the update function applies the 
game logic to update the game state. In this case, the `p1.attack(p2)` is
called, which triggers any effects when player1 attacks player2, decreases 
player2's prestige by player1's current attack, and sets player1's attack to zero.

-------
As another example, player2 may send a request to begin turn. The validator
checks that the game state has player1 ending his turn. The update function
collects all the 'start of turn' events for each card in play on both boards,
calls them in a random order, calls the increase population functions for each
planet in play under the active player's control, resource is added to the pool
and finally draws a card from the active player's deck to hand. Note that each 
sub-event modifies the Game, but only a single call to the update function 
`U`, is made.

Game Rules and Data Structures
--------
The game on the server is divided into three main components: 

The first is the game state, `g`. This state stores all the dynamic properties
of the game as it progresses, such as player prestige, attack and defense as 
well as cards in hands, decks, discards, and in play, and counters on cards in
play. Game states are stored in the server Redis after updates.

The second component are the cards themselves. Static card data is stored in 
class definitions, ie each named card in the game is a class with methods and
attributes, including location, text, attack/defense, resource required/generated 
and enters_play, leaves_play, activate, and start_turn effects. Named cards are
subclasses of the generic Card class.

The final component is the static game logic embedded in the validator and update
functions.
