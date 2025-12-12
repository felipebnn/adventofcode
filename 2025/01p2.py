#!/bin/env python3

with open('01_input.txt', 'r') as f:
    txt = f.read()

password = 0
x = 50

for move in txt.split('\n'):
    if not move:
        break

    d, *n = move
    n = int(''.join(n))

    password += n // 100
    n %= 100

    if d == 'L':
        n = -n

    if x + n >= 100 or x + n <= 0 and x != 0:
        password += 1

    x = (x + n) % 100

print(password)

