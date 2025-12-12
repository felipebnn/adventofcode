#!/bin/env python3
from collections import deque

with open('10_input.txt', 'r') as f:
    txt = f.read().strip('\n')

def do_button(indicators, button):
    for i in button:
        indicators ^= 1<<i
    return indicators

total = 0
for machine_str in txt.split('\n'):
    indicators, *buttons, _ = machine_str.split(' ')
    indicators = sum(
        1<<(i-1)
        for i in range(1, len(indicators)-1)
        if indicators[i] == '#'
    )
    buttons = [
        [ int(x) for x in button[1:-1].split(',') ]
        for button in buttons
    ]

    visited = set()
    q = deque([ (0, 0, 0) ])
    while q:
        ind, buts, steps = q.popleft()
        for i, button in enumerate(buttons):
            buts2 = buts | 1<<i
            if 1<<i & buts or buts2 in visited:
                continue
            ind2 = do_button(ind, button)
            visited.add(buts2)
            if ind2 == indicators:
                total += steps+1
                q = []
                break
            q.append(( ind2, buts2, steps+1 ))

print(total)
