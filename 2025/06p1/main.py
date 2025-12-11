#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip()

m = []
for line in txt.split('\n'):
    m.append([ txt for txt in line.split() ])

ans = 0
for j in range(len(m[0])):
    x = int(m[0][j])
    for i in range(1, len(m)-1):
        if m[-1][j] == '+':
            x += int(m[i][j])
        else:
            x *= int(m[i][j])
    ans += x

print(ans)
