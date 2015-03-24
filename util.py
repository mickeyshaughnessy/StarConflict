from Player import Player

def get_active(g):
    active = g['active']  # 'p1' or 'p2'
    opponent = 'p1' if active == 'p2' else 'p2'
    return (active, opponent)

def instantiate_players(g):
    p1 = Player('p1', g)
    p2 = Player('p2', g)
    return [p1, p2]

def instantiate_location(g, loc):
    places = []
    for player in ['p1', 'p2']:
        place = []
        for card in g[player][loc]:
            place.append(eval(card+'()'))
        places.append(place)
    

def instantiate(g):
    # returns an instantiated game - ie all Card and Player objects
    
    players = instantiate_players(g)
    
    decks = instantiate_location(g, 'deck')
    hands = instantiate_location(g, 'hand')
    discards = instantiate_location(g, 'discard')
    boards = instantiate_location(g, 'board')

    for pindex in [0,1]:
        for card in boards[pindex]:
            card.in_play()
        for card in discards[pindex]:
            card.in_discard()

    return players, decks, hands, discards, boards

        
