# validator.py
# This function takes events and game inputs and returns them if they are valid
# otherwise returns ('invalid', 'reason') 
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

def validator(e, g):
    active, opponent = get_active(g)
# check to see if it is a valid type event
    if e['event'] not in events:
        return ('invalid', 'not a valid event type') 

# check to see if the initiating player is active
# use 'p1' and 'p2' strings.
    if (active == 'p1' and e['player'] != g['pids'][0]) or 
       (active == 'p2' and e['player'] != g['pids'][1])):
        return ('invalid', "its not generating player's turn")

# check to see if attack target is valid
    if e['event'] == 'attack':
        opp_entities = g[opponent]
        if e['target'] not in (g[opponent]['board'] + [opponent]):
            return ('invalid', 'target not on board or opponent')
        # here check if there are any blockers on opponent's board

    return (e, g)

if __name__ == '__main__':
    pass
