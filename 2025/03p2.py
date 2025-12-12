#!/bin/env python3

def debug_print(bank, idx):
    prev_i = -1
    for i in idx:
        print(' ' * (i - prev_i - 1) + 'v', end='')
        prev_i = i
    print()
    print(bank)
    
with open('03_input.txt', 'r') as f:
    txt = f.read().strip()

total = 0
for bank in txt.split('\n'):
    idx = []
    last_idx = -1

    for i in range(12):
        m = last_idx+1
        for j in range(last_idx+2, len(bank)-11+i):
            if bank[j] > bank[m]:
                m = j
        last_idx = m
        idx.append(m)

    total += int(''.join(bank[i] for i in idx))
        
print(total)

