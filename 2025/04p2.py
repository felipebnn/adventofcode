#!/bin/env python3

with open('04_input.txt', 'r') as f:
    txt = f.read().strip()

grid = [ list(row_str) for row_str in txt.split('\n') ]

def debug_print():
    print('=====')
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='')
        print()

def get_xy(x, y):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return '.'
    return grid[y][x]

def set_xy(x, y, ch):
    grid[y][x] = ch

sibling_deltas = [
    (d_x, d_y)
    for d_y in [-1, 0, 1]
    for d_x in [-1, 0, 1]
    if d_x != 0 or d_y != 0
]

def count_papers(x, y):
    return sum(
        1
        for (d_x, d_y) in sibling_deltas
        if get_xy(x+d_x, y+d_y) == '@'
    )

ans = 0
should_visit = set()

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if get_xy(x, y) == '@' and count_papers(x, y) < 4:
            should_visit.add((x, y))

while should_visit:
    neo_should_visit = set()

    for (x, y) in should_visit:
        ch = get_xy(x, y)
        if ch != '@' or count_papers(x, y) >= 4:
            continue
        
        set_xy(x, y, '.')
        ans += 1
        for (d_x, d_y) in sibling_deltas:
            neo_should_visit.add((x+d_x, y+d_y))

    should_visit = neo_should_visit

print(ans)

