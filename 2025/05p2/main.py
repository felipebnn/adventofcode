#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip()

lines_iter = iter(txt.split('\n'))

ranges = []
for line in lines_iter:
    if not line:
        break
    ranges.append([ int(x) for x in line.split('-') ])

# merge ranges
ranges.sort()
m_ranges = [ranges[0]]
for r in ranges[1:]:
    if r[0] <= m_ranges[-1][1]:
        m_ranges[-1][1] = max(m_ranges[-1][1], r[1])
    else:
        m_ranges.append(r)

print(sum(b-a+1 for a, b in m_ranges))
