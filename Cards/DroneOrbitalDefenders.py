# Example subclass of Cards to show template for individual cards
from random import random
import sys
sys.path.append('/Users/michaelshaughnessy/StarConflict')

from Card import Card
from util import *

class DroneOrbitalDefenders(Card):
    def __init__(self):
        self.name = 'DroneOrbitalDefenders'
        Card.__init__(self, self.name)
# specific cards should always call the Card.__init__ method before setting 
# attributes (except self.name)
        self.attack = 0
        self.defense = 2
        self.is_blocker = True
        self.affiliation = 'Fedederation'
        self.resource_gen = 0
        self.resource_req = 1
        self.type = 'ship'
        self.text = 'When Drone Orbital Defender enters play, put an additional copy of it into play with probability = 0.4.'
        # The card remains in the game even after discard - ie gets reshuffled into deck, can be resurrected, etc.

    def enter_play(self, g, origin='hand'):
        active, opponent = get_active(g)
        if origin != 'token':
            g[active][origin].remove(self.name)
        g[active]['board'].append(self.name)
        
        if random() < 0.4:
            origin = 'token'
            self.enter_play(g, origin)
        
# This section and below are used for testing this card
if __name__ == '__main__':
    card = DroneOrbitalDefenders()
    g = {
        '_id' : 'thisexamplegameid',
        'active' : 'p1',
        'pids': ['user:mickey', 'user:matt'],
        'p1':{
            'board' : [],
            'hand' : ['DroneOrbitalDefenders'],
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

# commands below here that take g as an argument will
# only be called during a game from within the update function after
# the validator has determined that they are valid - ie
# enough resource is available.


    print ('initial game state %s' % g)
    card.draw(g)
    print ('after draw game state %s' % g)
    card.play(g)
    print ('after playing state %s' % g)
