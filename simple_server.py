from gevent import pywsgi
import redis
import routes

def handler(environ, start_response):
#    g = {
#        'redis': redis.StrictRedis(host=kwargs['redis'])
#         }
    #status, output, headers = dispatch(environ, g, routes.__dict__)
    output = '<strong>Play Star Conflict!</strong>\n'

    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return output


print 'Star Conflict server running...'
server = pywsgi.WSGIServer(
    ('', 8080), handler).serve_forever()

