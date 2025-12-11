#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

nodes = {}
for dev in txt.split('\n'):
    dev_name, *neighbors = dev.split(' ')
    dev_name = dev_name[:-1]
    nodes[dev_name] = neighbors

def dfs(n, target, cache):
    if n == target:
        return 1

    if n not in cache:
        cache[n] = sum(dfs(neighbor, target, cache) for neighbor in nodes.get(n, []))

    return cache[n]

svr_fft = dfs('svr', 'fft', {})
fft_dac = dfs('fft', 'dac', {})
dac_out = dfs('dac', 'out', {})

print(svr_fft * fft_dac * dac_out)
