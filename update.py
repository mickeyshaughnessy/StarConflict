# This function takes a valid game event and game state (e, g) as input and
# executes the event, modifying the game state.
from util import * 

# These are the only events a player can initiate
# events are of form:
# <action> <target_type1> <target1> ... <target_typeN>, <targetN>
# all events have an action
# and a variable number (0 to N) of targets and target_types
event_actions = [
    'end_turn', # end turn takes no other arguments
    'attack',  # can attack opposing player, planets, and cards_in_plays
    'play_card', # can play cards from hand
    'activate', # can activate abilities of cards on own board and in own discard
    'purchase', # can purchase artifacts or from shared purchase
    'concede', # no arguments
    'emit_taunt' # takes taunt string as argument
]
event_target_types = [
    'player',
    'planet',
    'card_in_play',
    'card_in_discard'
]


def update(e,g):  # e and g are both type == dict 
    instantiate(g) 
    return g 

