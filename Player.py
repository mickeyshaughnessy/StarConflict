import redis
from json import dumps, loads
from config import redis_hostname, redis_port
redis = redis.StrictRedis(host=redis_hostname)

class Player():
    # a player is init'd whenever its methods are needed. 

    def __init__(self, player_num, g): 
       # cardname is a string pointing to a card in the 'Cards' directory
        self.pid = g['pids'][0] if player_num == 'p1' else g['pids'][1]
        self.prestige = g[player_num]['prestige']
        self.player_num = player_num    

    def is_alive(self):
        return self.prestige > 0
    def is_active(self, g):
        return self.player_num == g['active'] 


if __name__ == '__main__':
    g = {
        'pids': ['user:mickey', 'user:gabe'],
        'active': 'p1',
        'p1': {
            'prestige': -4
        },
        'p2': {
            'prestige': 55 
        }
    }
    mickey = Player('p1', g)
    gabe = Player('p2', g)

    print mickey.is_alive()
    print gabe.is_alive()
    print gabe.is_active(g)





