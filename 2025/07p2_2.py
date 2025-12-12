#!/bin/env python3

with open('07_input.txt', 'r') as f:
    txt = f.read().strip('\n')

rows = txt.split('\n')

cache = {}

def dfs(i, j):
    if i >= len(rows):
        return 1

    if (i, j) not in cache:
        if rows[i][j] == '^':
            paths = dfs(i+1, j-1) + dfs(i+1, j+1)
        else:
            paths = dfs(i+1, j)

        cache[(i, j)] = paths

    return cache[(i, j)]

paths = dfs(1, rows[0].index('S'))
print(paths)
