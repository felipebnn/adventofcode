#!/bin/env python3
from collections import defaultdict

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

rows = txt.split('\n')

beams = { rows[0].index('S'): 1 }

for row in rows:
    neo_beams = defaultdict(int)
    for beam, count in beams.items():
        if row[beam] == '^':
            neo_beams[beam-1] += count
            neo_beams[beam+1] += count
        else:
            neo_beams[beam] += count
    beams = neo_beams

print(sum(x for x in beams.values()))
