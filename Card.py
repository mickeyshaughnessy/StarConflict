#import redis
#from json import dumps, loads
#from config import redis_hostname, redis_port
#redis = redis.StrictRedis(host=redis_hostname)

class Card():
    # a card is usually init'd once, at the beginning of a game

    def __init__(self, cardname=None):
        # cardname is a string pointing to a card in the 'Cards' directory
        self.name = cardname
        self.attack, self.defense, self.population = 0,0,0
        self.resource_req = 0
        self.resource_gen = 0
        self.text = ''
        self.location = ''
        self.type = ''
    
    def enters_play(self, g):
        pass
    def turn_start(self, g):
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
            self.die(self, g)
    def die(self, g):
        self.leaves_play(self, g)
        #modify g appropriately 


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




