db = pymongo.MongoClient().StarConflict

routes = {
        'users': [('POST', 'GET'), r'/users/?$'],
        'user': [('PUT', 'GET', 'DELETE'), r'/users/([-\w]+)/?$'],

        'key': ['GET', r'/users/([-\w]+)/key/?$'],
        'login': [('POST', 'GET'), r'/login/?'],
        'logout': [('POST', 'GET'), r'/logout/?'],
        'password_reset': [('GET', 'POST'), r'/password-reset/?$'],

        'stats': ['GET', r'/placements/([-\w]+)/stats/?$'],
        'query': [('GET', 'POST'), r'/query/?$'],
        'inventory': [('GET', 'POST'), r'/query/inventory/?$'],

        'dimensions': ['GET', r'/dimensions/?$'],
        'dimension': ['GET', r'/dimensions/(\w+)/?$'],
        'dimension_values': ['GET', r'/dimensions/(\w+)/values/?$'],

        'contact_us': ['POST', r'/contact/submit/?'],
        'preview': ['GET', r'/preview/(\w+)/?$']
    }
