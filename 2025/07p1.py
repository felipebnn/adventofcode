#!/bin/env python3

with open('07_input.txt', 'r') as f:
    txt = f.read().strip('\n')

rows = txt.split('\n')

splits = 0
beams = { rows[0].index('S') }

for row in rows:
    neo_beams = set()
    for beam in beams:
        if row[beam] == '^':
            splits += 1
            neo_beams.add(beam-1)
            neo_beams.add(beam+1)
        else:
            neo_beams.add(beam)
    beams = neo_beams

print(splits)
