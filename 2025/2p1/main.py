#!/bin/env python3

with open('input.txt', 'r') as f:
    txt = f.read().strip()

ranges = txt.split(',')
passwd = 0

for r in ranges:
    s_a, s_b = r.split('-')
    b = int(s_b)

    while len(s_a) <= len(s_b):
        if len(s_a) % 2 != 0:
            s_a = '1' + '0'*len(s_a)
            continue

        half_length = len(s_a) // 2
        left_half = s_a[:half_length]
        num = int(left_half + left_half)
        limit = min(b, int('9' * len(s_a)))

        if num < int(s_a):
            num += 1 + 10**half_length
        
        passwd += sum(range(num, limit+1, 1 + 10**half_length))
        s_a = '10' + '0'*len(s_a)

print(passwd)
