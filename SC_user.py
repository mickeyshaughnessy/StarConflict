# This class defines the platform wide user objects
import redis
from json import dumps, loads
from config import redis_hostname, redis_port
redis = redis.StrictRedis(host=redis_hostname)

class SC_User():
    def __init__(self, username=None):
        self.username = username
        
        new_user = not bool(redis.get(self.username))
        
        if new_user:
            self.collection = self.default_collection()
            user = {
                'username': self.username,
                'collection': self.collection,
                'wins': 0,
                'losses': 0
            }
            redis.set(self.username, user)
        else:
            user = loads(redis.get(self.username))
            print user
            self.collection = user['collection']
            
        
    def default_collection(self):
        return {'Drone Orbital Defenders': 4}

if __name__ == '__main__':
    Mickey = SC_User('mickey')
    print Mickey.collection
    print Mickey.default_collection()
