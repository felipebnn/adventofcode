#!/bin/env python3
import heapq

from collections import defaultdict
from math import prod

with open('08_input.txt', 'r') as f:
    txt = f.read().strip('\n')

class DSU:
    def __init__(self, coord):
        self.parent = None
        self.coord = [ int(x) for x in coord.split(',') ]

    def get_parent(self):
        if self.parent is None:
            return self
        self.parent = self.parent.get_parent()
        return self.parent

    def add(self, other):
        other.get_parent().parent = self.get_parent()

nodes = [ DSU(coord) for coord in txt.split('\n') ]

distances = []
for i in range(len(nodes)-1):
    a = nodes[i]
    for j in range(i+1, len(nodes)):
        b = nodes[j]
        distances.append((
            sum((c1-c2) ** 2 for c1, c2 in zip(a.coord, b.coord)),
            a, b
        ))
heapq.heapify(distances)

for _ in range(1000):
    _, a, b = heapq.heappop(distances)
    if a.get_parent() == b.get_parent():
        continue

    a.add(b)

circuits = defaultdict(list)
for n in nodes:
    circuits[n.get_parent()].append(n)

top_3 = sorted([ -len(l) for l in circuits.values() ])[:3]
print(-prod(top_3))
