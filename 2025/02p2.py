#!/bin/env python3

def is_invalid(x):
    for i in range(1, len(x)//2+1):
        if len(x) % i != 0:
            continue
        
        sub = x[:i]
        y = sub * (len(x) // i)
        if x == y:
            return True

    return False

with open('02_input.txt', 'r') as f:
    txt = f.read().strip()

ranges = txt.split(',')
passwd = 0

for r in ranges:
    a, b = (int(x) for x in r.split('-'))

    for a in range(a, b+1):
        if is_invalid(str(a)):
            passwd += a

print(passwd)
