# Example subclass of Cards to show template for individual cards
from random import random
import sys
sys.path.append('/Users/michaelshaughnessy/StarConflict')

from Card import Card
from util import *

class GoblinMechanic(Card):
    def __init__(self):
        self.name = 'GoblinMechanic'
        Card.__init__(self, self.name)
# specific cards should always call the Card.__init__ method before setting 
# attributes (except self.name)
        self.attack = 4
        self.defense = 1
        self.is_blocker = False
        self.affiliation = 'Goblinoid'   
        self.resource_gen = 0
        self.resource_req = 2
        self.type = 'troop'
        self.text = 'At the beginning of your turn, all your ships get -2 attack.'

    def turn_start(self, g, G):
        active, opponent = get_active(g)
        
        pass
# This section and below are used for testing this card
if __name__ == '__main__':
    g = {
        '_id' : 'thisexamplegameid',
        'active' : 'p1',
        'pids': ['user:mickey', 'user:matt'],
        'p1':{
            'board' : [],
            'hand' : ['DroneOrbitalDefenders', 'GoblinMechanic'],
            'deck' : ['DroneOrbitalDefenders', 'GasPlanet'],
            'discard': [],
            'prestige' : 10,
            'population' : 2,
            'resource' : 3,
            'attack' : 5,
            'defense': 0
            },
        'p2':{
            'board' : [],
            'hand' : ['DroneOrbitalDefenders'],
            'deck' : ['DroneOrbitalDefenders', 'GasPlanet'],
            'discard': [],
            'prestige' : 10,
            'population' : 2,
            'resource' : 3,
            'attack' : 5,
            'defense': 0
            }
        }

    G = instantiate(g)

# commands below here that take g as an argument will
# only be called during a game from within the update function after
# the validator has determined that they are valid - ie
# enough resource is available.


    print ('initial game state %s' % g)
    card.draw(g, G)
    print ('after draw game state %s' % g)
    card.play(g, G)
    print ('after playing state %s' % g)
