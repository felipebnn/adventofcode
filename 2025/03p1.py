#!/bin/env python3

with open('03_input.txt', 'r') as f:
    txt = f.read().strip()

total = 0

def debug_print(bank, i, j):
    print(' ' * i + 'v' + ' ' * (j - i - 1) + 'v')
    print(bank)

for bank in txt.split('\n'):
    i = 0
    j = 1
    k = 1

    while k < len(bank):
        if bank[k] > bank[i] and k+1 < len(bank):
            i = k
            j = k+1
        elif bank[k] > bank[j]:
            j = k

        k += 1

    x = int(bank[i] + bank[j])
    total += x
        
print(total)

