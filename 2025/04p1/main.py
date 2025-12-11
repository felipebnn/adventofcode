#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip()

grid = txt.split('\n')

def get_xy(x, y):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return '.'
    return grid[y][x]

def count_papers(x, y):
    count = 0

    for d_y in [-1, 0, 1]:
        for d_x in [-1, 0, 1]:
            if d_y == 0 and d_x == 0:
                continue
            if get_xy(x+d_x, y+d_y) == '@':
                count += 1

    return count


ans = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        ch = get_xy(x, y)
        if ch == '@' and count_papers(x, y) < 4:
            # ch = 'x'
            ans += 1
        # print(ch, end='')
    # print()

print(ans)

