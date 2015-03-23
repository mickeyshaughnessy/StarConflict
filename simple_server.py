from flask import Flask, request
from gevent import pywsgi
import redis
import routes

app = Flask(__name__)

@app.route('/')
def greeting():
    output = '<strong>Play Star Conflict!</strong>\n'
    return output 

@app.route('/users')
def get_users():
    users = {}
    return dumps(users)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()

