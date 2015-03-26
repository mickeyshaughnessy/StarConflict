from flask import Flask, request
from gevent import pywsgi
import redis
from time import sleep
from config import *
from json import loads, dumps
from SC_user import User

redis = redis.StrictRedis(host=redis_hostname)

app = Flask(__name__)

@app.route('/')
def greeting():
    output = '<strong>Play Star Conflict!</strong>\n'
    return output 

@app.route('/users/<username>', methods = ['GET', 'POST'])
def api_users(username):
    if request.method == 'GET':
        user = dumps(redis.get('user:'+username))
        return user  
    if request.method == 'POST':
        user = dumps(redis.get('user:'+username))
        if user == 'null':
            user = User(username)
            sleep(0.1)  # To 
            user = dumps(redis.get('user:'+username)) 
        return user

if __name__ == '__main__':
#app.run()
    app.run(debug=True)

