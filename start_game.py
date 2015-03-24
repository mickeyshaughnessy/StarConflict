from random import random, choice, shuffle
import redis
from json import loads, dumps 
from config import * 
from hashlib import sha1
from datetime import datetime

redis = redis.StrictRedis(host=redis_hostname)

def gen_id(pids):
    # This function generates a unique game id string of form: 'game:<numbers_and_letters>'
    cand = sha1(pids[0] + pids[1] + str(datetime.now())).hexdigest()
    while redis.get('game:'+cand):
        cand = sha1(pids[0] + pids[1] + str(datetime.now())).hexdigest()
    return cand

def make_decks(p1, p2, deck1s, deck2s, techs, unaff_fracs, g):
    # given the initial game object and player choices, this function makes the
    # initial decks and shuffles them.

    # p1, p2 are player objects
    # deck1s, deck2s, and techs are two element arrays, consisting
    # of affiliation choice strings, ie deck1s = ['Federation', 'Federation']
    # unaff_frac is a two element array of fractions specifying the fraction
    # of each players unaffiliated collection to use.

    # each player chooses two (unique) race decks and one tech deck.
    # if any race or tech deck is chosen by both players, both players
    # use a copy of their combined decks.
    all_decks = deck1s + deck2s + techs
    # build decks by iterating over collections
    for player in [p1,p2]:
        p_string = 'p1' if player == p1 else 'p2'
        p_ind = 0 if player == p1 else 1
        p_decks = [deck1s[p_ind], deck2s[p_ind], techs[p_ind]] 
        collection = player['collection']
        for card in collection:
            aff = collection[card]['affiliation']
            if all_decks.count(aff) > 1:
                g['p1']['deck'].append(card)
                g['p2']['deck'].append(card)
            elif aff in p_decks: 
                g[p_string]['deck'].append(card)

        # at this point each deck contains the race and tech cards
        # now add in the unaffs
        p_unaffs = [x for x in collection if
                    collection[x]['affiliation'] == 'Unaffiliated']
        for j in xrange(len(g[p_string]['deck'])):
            if random() < unaff_fracs[p_ind]:
                g[p_string]['deck'].append(choice(p_unaffs))

        # now shuffle!
        for deck in [g['p1']['deck'], g['p2']['deck']]:
            shuffle(deck)

def start_game(pids, deck1s, deck2s, techs, unaff_fracs):
    p1 = loads(redis.get(pids[0])) 
    p2 = loads(redis.get(pids[1])) 
   
    # for each tech deck selected and the two decks selected by the the 
    # players, shuffle the relevant sections of each player's active decks 
    # together. 

    # ie if p1 selects ('Federation', 'Rebels', 'Tissue Culture') and
    # if p2 selects ('Federation', 'Goblinoids', and 'Fusion') then p1's
    # deck will be:
    #   union(Fedederation_p1, Federation_p2, Rebels_p1, and Tissue Culture_p1')
    # p2's deck will be:
    #   union(Federation_p1, Federation_p2, Goblinoids_p2 and Fusion_p2)
    #   
    # Where the 'Affiliation_pi' represent the ith players active deck 
    # (defaults to collection) for the Affiliation. 

    # Initially, both player's unaffiliated active decks are shuffled into
    # their game decks with a given mixing fraction (default = 0.2). 
    g = {
        'p1': {
            'hand': [],
            'deck': [],
            'board': [],
            'discard': [],
            'prestige': 49,
            'population': 0,
            'resource': 0,
            'attack': 0,
            'defense': 0
            },
        'p2': {
            'hand': [],
            'deck': [],
            'board': [],
            'discard': [],
            'prestige': 49,
            'population': 0,
            'resource': 0,
            'attack': 0,
            'defense': 0
            }
        }

    make_decks(p1, p2, deck1s, deck2s, techs, unaff_fracs, g)
    g['_id'] = gen_id(pids)
    g['pids'] = [pids[0], pids[1]]
    g['active'] = choice(['p1', 'p2'])
    
    # push g to Redis
    redis.set('game:'+g['_id'], dumps(g))

    return g

if __name__ == '__main__':
    pids = ['user:mickey', 'user:matt']
    deck1s = ['Federation', 'Federation']
    deck2s = ['Goblinoid', 'Rebel']
    techs = ['Fusion', 'Tissue_Culture']
    unaff_fracs = [0.2, 0.3]
    
    g = start_game(pids, deck1s, deck2s, techs, unaff_fracs)
    print g
