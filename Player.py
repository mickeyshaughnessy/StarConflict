import redis
from json import dumps, loads
from config import redis_hostname, redis_port
redis = redis.StrictRedis(host=redis_hostname)

class Player():
    # a player is init'd whenever its methods are needed. 

    def __init__(self, player_num, g):
        print g
       # cardname is a string pointing to a card in the 'Cards' directory
        self.pid = g['pids'][0] if player_num == 'p1' else g['pids'][1] # username
        self.player_num = player_num    # 'p1' or 'p2'
        self.prestige = g[player_num]['prestige']
        self.attack = g[player_num]['attack']
        self.defense = g[player_num]['defense']
        self.resource = g[player_num]['resource']
        self.population = g[player_num]['population']
        self.deck = g[player_num]['deck']
        self.board = g[player_num]['board']
        self.hand = g[player_num]['hand']
        self.discard = g[player_num]['discard']
        
    def is_alive(self):
        return self.prestige > 0
    def is_active(self, g):
        return self.player_num == g['active'] 


if __name__ == '__main__':
    g = {
        'pids': ['user:mickey', 'user:gabe'],
        'active': 'p1',
        'artifacts_deck': [],
        'artifacts_purchase': [],
        'shared_deck': [],
        'shared_purchase': [],
        'p1': {
            'prestige': -4,
            'attack': 0,
            'defense': 0,
            'population': 0,
            'resource': 0,
            'deck' : [],
            'hand' : [],
            'board' : [],
            'discard' : []
        },
        'p2': {
            'prestige': 55,
            'attack': 0,
            'defense': 0,
            'population': 0,
            'resource': 0,
            'deck' : [],
            'hand' : [],
            'board' : [],
            'discard' : []
        }
    }

    mickey = Player('p1', g)
    gabe = Player('p2', g)

    print mickey.is_alive()
    print gabe.is_alive()
    print gabe.is_active(g)





