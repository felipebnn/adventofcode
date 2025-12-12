#!/bin/env python3

with open('12_input.txt', 'r') as f:
    txt = f.read().strip('\n')

lines = txt.split('\n')

pieces_size = []
for i in range(0, len(lines), 5):
    if ': ' in lines[i]:
        break
    pieces_size.append(sum(1 for c in ''.join(lines[i+1:i+5]) if c == '#'))

total = 0
for problem in lines[i:]:
    size, *pieces_count = problem.split(' ')
    w, h = [ int(x) for x in size[:-1].split('x') ]

    pieces_area = sum(int(count) * size for count, size in zip(pieces_count, pieces_size))
    if w * h > pieces_area:
        total += 1

print(total)
