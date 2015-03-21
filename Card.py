import redis
from json import dumps, loads
from config import redis_hostname, redis_port
redis = redis.StrictRedis(host=redis_hostname)

class Card():
    def __init__(self, cardname=None):
        self.cardname = cardname
        self.data = loads(redis.get(self.cardname))
        if self.data['type'] in ['ship', 'troop', 'character']:
            self.attack = self.data['attack']
            self.defense = self.data['defense']

    def enters_play(self, g):
        print self.data['enters_play']
    def turn_start(self, g):
        for event in self.data.events.turn_start:
            event()
    def activate(self, g, target):
        self.data.events 
    def leaves_play(self, g):
        for event in self.data['enters_play']:
            print event
    def change_attack(self, g, attack):
        self.attack += attack
    def change_defense(self, g, defense):
        self.defense += defense
        if self.defense < 1:
            self.die(self, g)
    def die(self, g):
        self.leaves_play(self, g)
        g['discard'][g['active']].add_card(self, g)


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




