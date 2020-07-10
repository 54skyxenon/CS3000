#!/usr/local/bin/python3
# Author: Brandon Liang

import random

def galeShapley(hospitalPreferences, doctorPreferences):
    # our matchings
    matchings = dict()
    unmatched = set(hospitalPreferences.keys())

    while unmatched:
        # hospital h is arbitrary
        h = random.choice(tuple(unmatched))

        # doctor d is the highest-ranked doctor to which h hasn't offered a job to yet
        d = hospitalPreferences[h].pop(0)

        # h makes an offer to d
        if d not in matchings:
            matchings[d] = h
            unmatched -= {h}
        elif doctorPreferences[d].index(matchings[d]) < doctorPreferences[d].index(h):
            # reject, do nothing
            pass
        elif doctorPreferences[d].index(matchings[d]) > doctorPreferences[d].index(h):
            unmatched |= {matchings[d]}
            matchings[d] = h
            unmatched -= {h}

    return matchings

hospital = dict()
hospital['MGH'] = ['A', 'B', 'C']
hospital['BW'] = ['B', 'C', 'A']
hospital['BID'] = ['A', 'C', 'B']

doctors = dict()
doctors['A'] = ['BW', 'BID', 'MGH']
doctors['B'] = ['BID', 'MGH', 'BW']
doctors['C'] = ['MGH', 'BID', 'BW']

hospital2 = dict()
hospital2['MGH'] = ['B', 'A', 'D', 'E', 'C']
hospital2['BW'] = ['D', 'B', 'A', 'C', 'E']
hospital2['BID'] = ['B', 'E', 'C', 'D', 'A']
hospital2['MTA'] = ['A', 'D', 'C', 'B', 'E']
hospital2['CH'] = ['B', 'D', 'A', 'E', 'C']

doctors2 = dict()
doctors2['A'] = ['CH', 'MGH', 'BW', 'MTA', 'BID']
doctors2['B'] = ['BID', 'BW', 'MTA', 'MGH', 'CH']
doctors2['C'] = ['BW', 'BID', 'MTA', 'CH', 'MGH']
doctors2['D'] = ['MGH', 'CH', 'MTA', 'BID', 'BW']
doctors2['E'] = ['MTA', 'BW', 'CH', 'BID', 'MGH']

print(galeShapley(hospital, doctors))
print(galeShapley(hospital2, doctors2))

hospital3 = dict()
hospital3['H1'] = ['D2', 'D3', 'D1']
hospital3['H2'] = ['D1', 'D3', 'D2']
hospital3['H3'] = ['D3', 'D2', 'D1']

doctors3 = dict()
doctors3['D1'] = ['H1', 'H2', 'H3']
doctors3['D2'] = ['H1', 'H3', 'H2']
doctors3['D3'] = ['H2', 'H3', 'H1']

print(galeShapley(hospital3, doctors3))