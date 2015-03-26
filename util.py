from Player import Player

def get_active(g):
    active = g['active']  # 'p1' or 'p2'
    opponent = 'p1' if active == 'p2' else 'p2'
    return (active, opponent)

def instantiate_players(g):
    g['p1'] = Player('p1', g)
    g['p2'] = Player('p2', g)

def instantiate_location(g, loc):
    places = []
    for player in ['p1', 'p2']:
        place = []
        for card in g[player][loc]:
            place.append(eval(card+'()'))
        places.append(place)
    

def instantiate(g):
    # Transforms g into an instantiated game - ie all relevant values are Card and Player objects
    
    instantiate_players(g)
    instantiate_location(g, 'decks')
    instantiate_location(g, 'hands')
    instantiate_location(g, 'discards')
    instantiate_location(g, 'boards')
    instantiate_location(g, 'artifacts_deck')
    instantiate_location(g, 'artifacts_purchase')
    instantiate_location(g, 'shared_deck')
    instantiate_location(g, 'shared_purchase')

# call all in play methods
    for pindex in [0,1]:
        for card in g[pindex]['board']:
            card.in_play()
        for card in discards[pindex]:
            card.in_discard()

# check for both players alive
    winner = g['winner'] 
    if not g['p2'].is_alive() and not g['p1'].is_alive():
        winner = 'tie'
    elif not g['p2'].is_alive():
        winner = 'p1'
    elif not g['p1'].is_alive():
        winner = 'p2'
        
