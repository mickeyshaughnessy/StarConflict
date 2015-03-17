models = {
    'game' : {
        Required('_id'): basestring,
        Required('player_ids'): [basestring],
        Required('hands'): [basestring],
        Required('decks'): [basestring],
        Required('boards'): [basestring],
        Required('discards'): [basestring],
        Required('technologies'): [basestring],
        Required('authority'): [int],
        Required('population'): [int],
        Required('resources'): [int],
        Required('attack'): [int],
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
        'in_play_function': 
        'discard_function':
}
