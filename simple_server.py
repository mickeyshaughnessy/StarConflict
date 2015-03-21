from flask import Flask
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

if __name__ == '__main__':
    app.run()

#def handler(environ, start_response):
##    g = {
##        'redis': redis.StrictRedis(host=kwargs['redis'])
##         }
#    #status, output, headers = dispatch(environ, g, routes.__dict__)
#    
#    output = '<strong>Play Star Conflict!</strong>\n'
#
#    status = '200 OK'
#    headers = [('Content-Type', 'text/html')]
#    start_response(status, headers)
#    return output
#
#
#print 'Star Conflict server running...'
#server = pywsgi.WSGIServer(
#    ('', 8080), handler).serve_forever()

