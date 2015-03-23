from util import *

class Card():
    # a card is init'd whenever its methods are needed. 

    def __init__(self, cardname=None):
        # cardname is a string pointing to a card in the 'Cards' directory
        self.name = cardname
        (self.attack, self.defense, self.population, self.resource_req,
         self.resource_gen)  = 0,0,0,0,0
        self.text = ''
        self.type = ''
    
    def play(self, g, origin='hand'):
        active, opponent = get_active(g)
        g[active]['board'].append(self.name)
        g[active][origin].remove(self.name)
        self.enter_play(g, origin)   

    def draw(self, g, origin='deck'):
        active, opponent = get_active(g)
        g[active]['deck'].remove(self.name)
        g[active]['hand'].append(self.name)

    def discard(self, g, origin='hand'):
        active, opponent = get_active(g)
        g[active][origin].remove(self.name)
        g[active]['discard'].append(self.name)
        if origin == 'board':
            self.leave_play(g)
   
    def enter_play(self, g, origin='hand'):
        pass
    def leave_play(self, g):
        pass
    def turn_start(self, g):
        # The code below is appropriate for the update logic, not the Card class
        # active, opponent = get_active(g)
        #       for card in g[active]['board']:
        #           eval(card+'.turn_start()')           
        pass

    def activate(self, g):
        pass
    def generated_resource(self,g):
        pass
    def leaves_play(self, g):
        pass
    def add_counter(self, g):
        pass
        if self.defense < 1:
            self.discard(self, g, )


if __name__ == '__main__':
    DRO = {
        'cardname': 'Drone Orbital Defenders',
        'type': 'ship',
        'affiliation': 'federation',
        'attack': 1,
        'defense': 1,
        'text': 'When Drone Orbital Defenders enters play, put an additional copy of it into play with probability = 0.3.',
        'resource_generated': 0,
        'capacity': None,
        'blocker': True,
        'resource_required': 1,
        'population_required': 1,
        'flavor_text': '',
        'adult': False,
        'enters_play': 'DROs_enter_play', 
        'turn_start': '',
        'turn_end': '',
        'leaves_play': ''
    }
    redis.set('Drone Orbital Defenders', dumps(DRO))

    card1 = Card('Drone Orbital Defenders')

    card1.enters_play(0)




