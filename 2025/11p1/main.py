#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

nodes = {}
for dev in txt.split('\n'):
    dev_name, *neighbors = dev.split(' ')
    dev_name = dev_name[:-1]
    nodes[dev_name] = neighbors

cache = {}
def dfs(n):
    if n == 'out':
        return 1

    if n not in cache:
        cache[n] = sum(dfs(neighbor) for neighbor in nodes[n])

    return cache[n]

print(dfs('you'))
