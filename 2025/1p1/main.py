#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read()

password = 0
x = 50

for move in txt.split('\n'):
    if not move:
        break

    d, *n = move
    n = int(''.join(n))

    if d == 'L':
        n = -n

    x = (n + x) % 100
    if x == 0:
        password += 1

print(password)

