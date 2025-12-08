#!/bin/env python3

with open('input.txt', 'r') as f:
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
distances.sort()

connections = 0
for _, a, b in distances:
    if a.get_parent() == b.get_parent():
        continue
    
    connections += 1
    a.add(b)
    
    if connections == len(nodes)-1:
        print(a.coord[0] * b.coord[0])
        break
