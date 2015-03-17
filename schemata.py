models = {
    'game' : {
        Required('_id'): basestring,
        Required('players'): [basestring],
        Required('hands'): [basestring],
        Required('decks'): [basestring],
        Required('boards'): [basestring],
        Required('discards'): [basestring],
        Required('technologies'): [basestring],
        Required('authority'): [int],
        Required('population'): [int],
        Required(''): [int],
        Required('authority'): [int],
    }
}
