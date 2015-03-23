models = {
    'game' : {
        '_id': basestring,
        'pids': [basestring],
        'active': basestring,,
        'p1': {
            'hand': [basestring],
            'deck': [basestring],
            'board': [basestring],
            'discard': [basestring],
            'prestige': int,
            'population': int,
            'resource': int,
            'attack': int,
            'defense': int
        }
        'p2': {
            'hand': [basestring],
            'deck': [basestring],
            'board': [basestring],
            'discard': [basestring],
            'prestige': int,
            'population': int,
            'resource': int,
            'attack': int,
            'defense': int
        }

    },
    'user': {
        Required('_id'): basestring,
        Required('purchased'): [basestring],
        Required('user_name'): basestring,
        Required('win_loss_history'): [ basestring : basestring]
    },
    'card': {
        Required('name'): basestring,
        Required('text'): basestring,
        'type': basestring,
        'defense': basestring,
        'into_play_function': basestring, 
        'in_play_': basestring, 
        'discard_function': basestring
}
