#!/bin/env python3
from math import prod

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

tiles = [ [ int(x) for x in t.split(',') ] for t in txt.split('\n') ]
largest_area = 0

for i in range(len(tiles)-1):
    a = tiles[i]
    for j in range(i+1, len(tiles)):
        b = tiles[j]
        d = prod(( abs(x-y)+1 for x, y in zip(a, b) ))
        largest_area = max(largest_area, d)

print(largest_area)
