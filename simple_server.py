from gevent import pywsgi

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<b>Play Star Conflict!</b>\n'

server = pywsgi.WSGIServer(
    ('', 8080), hello_world)

server.serve_forever()
