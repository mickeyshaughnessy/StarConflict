# This class defines the platform wide user objects
# Its init method is called when a new user is generated.

import redis
from json import dumps, loads
from config import redis_hostname, redis_port
redis = redis.StrictRedis(host=redis_hostname)

class SC_User():
    def __init__(self, username=None):
        self.username = username
        
        new_user = not bool(redis.get('user:'+self.username))
        
        if new_user:
            self.collection = self.default_collection()
            self.wins = 0
            self.losses = 0
            self.update_redis()
        else:
            user = loads(redis.get('user:'+self.username))
            self.collection = user['collection']
            self.wins = user['wins']
            self.losses = user['losses']

    def add_to_collection(self, cardname, number):
        if cardname in self.collection:
            self.collection[cardname] += number
        else:
            self.collection[cardname] = number
        self.update_redis() 

    def update_redis(self):
        user = {
                'username': self.username,
                'collection': self.collection,
                'wins': self.wins,
                'losses': self.losses
            }
        redis.set('user:'+self.username, dumps(user))

    def default_collection(self):
        return {'Drone_Orbital_Defenders':{
                    'number': 4,
                    'affiliation': 'Federation'
                    },
                'Gas_Planet':{
                    'number': 2,
                    'affiliation': 'Unaffiliated'
                    },
                'Artificial_Planet':{
                    'number': 4,
                    'affiliation': 'Unaffiliated'
                    },
                'Troll_Marauders':{
                    'number': 2,
                    'affiliation': 'Goblinoid'
                    },
                } 

if __name__ == '__main__':
    Mickey = SC_User('mickey')
    Matt = SC_User('matt')
    Gabe = SC_User('gabe')
    Amit = SC_User('amit')
    print Mickey.collection
    print Mickey.default_collection()
    print Mickey.collection['Drone_Orbital_Defenders']
    print Mickey.collection.keys()
    print type(loads(redis.get('user:mickey')))
