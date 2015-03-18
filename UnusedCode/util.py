import logging
from logging_helpers import MongoDBHandler
from StarConflict.config import events_hostname

log_format_string = (
    '%(asctime)s'
    '|%(module)s'
    '|%(processName)s'
    '|%(process)d'
    '|%(levelname)s'
    ': %(message)s'
)

def dispatch(environ, g, route_info):
    method = environ['REQUEST_METHOD']
    route_string = environ['PATH_INFO']
    args = '404 Not Found'
    for name, (methods, pattern) in route_info['routes'].iteritems():
        if method in methods:
            match = re.findall(pattern, route_string)
            if match:
                try:
                    args = route_info[name](environ, g, match[0])
                except:
                    logging.exception('Unhandled exception at dispatcher.')
                    logging.debug(environ)
                    args = '500 Internal Server Error'
                break
    i = hasattr(args, '__iter__')
    status = args[0] if i else args
    output = args[1] if len(args) > 1 and i else ''
    headers = args[2] if len(args) > 2 and i else []
    return status, output, headers

def init_logging(log_level, send_to_db=True, db_level='warning'):
    logger = logging.getLogger()
    level=getattr(logging, log_level.upper())
    logger.setLevel(level)

    ## create console handler and set level to debug
    logger.handlers = []

    ch = logging.StreamHandler()
    #ch = logger.handlers[0]

    ch.setLevel(level)

    ## create formatter
    formatter = logging.Formatter(log_format_string)

    ## add formatter to ch
    ch.setFormatter(formatter)

    ## add ch to logger
    logger.addHandler(ch)

    if send_to_db:
        # Send logs to a mongodb collection.
        handler = MongoDBHandler(log_hostname, 'StarConflict')

        # Only send logs with warning level and above.
        handler.setLevel(getattr(logging, db_level.upper()))

        # Add this custom handler to the root logger.
        logger.addHandler(handler)
