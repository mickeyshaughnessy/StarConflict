from flask import Flask, request
from gevent import pywsgi
import redis
from time import sleep
from config import *
from json import loads, dumps
from SC_user import User
from update import update

redis = redis.StrictRedis(host=redis_hostname)

app = Flask(__name__)

@app.route('/')
def greeting():
    output = '<strong>Play Star Conflict!</strong>\n'
    return output 

@app.route('/users/<username>', methods = ['GET', 'POST'])
def api_users(username):
    if request.method == 'GET':
        user = redis.get('user:'+username)
    if request.method == 'POST':
        user = dumps(redis.get('user:'+username))
        if user == 'null': #if user not there, make it
            user = User(username)
            sleep(0.1)  # To 
            user = redis.get('user:'+username) 
    return user

@app.route('/games/<game_id>', methods = ['GET', 'POST'])
def api_games(game_id):
    if request.method == 'GET':
        game = redis.get('game:'+game_id)
    if request.method == 'POST':
        game = redis.get('game:'+game_id)
        g = loads(game)
        e = request.json 
        game = dumps(update_game(g,e)) 
        #return request.args.get('event','')
    return game


if __name__ == '__main__':
#app.run()
    app.run(debug=True)

