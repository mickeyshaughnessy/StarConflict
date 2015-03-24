# This function takes a valid game event and game state (e, g) as input and
# executes the event, modifying the game state.
from util import * 

# These are the only events a player can initiate
events = [
    'start_turn',
    'end_turn',
    'activate_card',
    'play_card',
    'purchase_artifact',
    'attack'
]

def update(e,g):
    instantiate(g) 
    

