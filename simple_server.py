from gevent import pywsgi
import redis
import routes

def handler(environ, start_response):
#    g = {
#        'redis': redis.StrictRedis(host=kwargs['redis'])
#         }
    #status, output, headers = dispatch(environ, g, routes.__dict__)
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
#output = 'Play Star Conflict!'
    return '<b>Play Star Conflict!</b>\n'
    
#   return output

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print environ
    return '<b>Play Star Conflict!</b>\n'

server = pywsgi.WSGIServer(
    ('', 8080), handler).serve_forever()

server.serve_forever()
