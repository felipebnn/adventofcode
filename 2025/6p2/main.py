#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

# transpose matrix
m = list(zip(*txt.split('\n')))

op = ''
ans = 0
x = 0
for row in m:
    if row[-1] != ' ':
        op = row[-1]
        ans += x
        x = int(''.join(row[:-1]))
        continue

    try:
        y = int(''.join(row[:-1]))
    except ValueError:
        continue

    x = x+y if op == '+' else x*y

print(ans + x)
