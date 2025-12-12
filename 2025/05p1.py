#!/bin/env python3

with open('05_input.txt', 'r') as f:
    txt = f.read().strip()

lines_iter = iter(txt.split('\n'))

ranges = []
for line in lines_iter:
    if not line:
        break
    ranges.append([ int(x) for x in line.split('-') ])
ranges.sort()

ingredients = list(int(x) for x in lines_iter)

m_ranges = [ranges[0]]
for r in ranges[1:]:
    if r[0] <= m_ranges[-1][1]:
        m_ranges[-1][1] = max(m_ranges[-1][1], r[1])
    else:
        m_ranges.append(r)
ranges = m_ranges

def bin_search(x):
    i = 0
    j = len(ranges)

    while i+1 < j:
        mid = (i + j) // 2
        r = ranges[mid]

        if r[0] <= x <= r[1]:
            return True

        if x > r[1]:
            i = mid
        elif r[0] > x:
            j = mid

    return ranges[i][0] <= x <= ranges[i][1]

qty = 0
for ingredient in ingredients:
    if bin_search(ingredient):
        qty += 1
print(qty)
