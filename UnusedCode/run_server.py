
# This script runs the Star Conflict game server

import argparse
import logging
import redis
import routes
from util import dispatch, init_logging
from gevent import pywsgi

def run_server(**kwargs):
    g = {
            'redis': redis.StrictRedis(host=kwargs['redis'])
        }

    def handler(environ, start_response):
        status, output, headers = dispatch(environ, g, routes.__dict__)
        if output and not any(k.lower() == 'content-type' for k, v in headers):
            headers += [('Content-Type', 'application/json')]
        start_response(status, headers)
        return [output]

    log = 'default' if logging.getLogger().getEffectiveLevel() \
            == logging.DEBUG else None

    server = pywsgi.WSGIServer(
            (kwargs['hostname'], kwargs['port']), handler, log=log
        ).serve_forever()

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--log-level', default='info')
    p.add_argument('--hostname', default='0.0.0.0')
    p.add_argument('--redis', default=redis_main_hostname)
    p.add_argument('--port', type=int, default=3030)
    args = p.parse_args()

    init_logging(args.log_level, db_level='info')
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    logging.info('Starting StarConflict service at %(hostname)s:%(port)s'%args.__dict__)
    try: run_server(**args.__dict__)
    except KeyboardInterrupt: pass

# Load required objects

# Listen for clients
  # On contact 
     # update game state
     # push game to clients


