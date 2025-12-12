#!/bin/env python3

with open('06_input.txt', 'r') as f:
    txt = f.read().strip('\n')

m = txt.split('\n')

rows = len(m)
columns = len(m[0])

ans = 0

last_op_idx = columns + 1
op_idx = len(str(m[-1]).strip())-1

while op_idx >= 0:
    nums = []
    for j in range(op_idx, last_op_idx-1):
        x = 0
        for i in range(rows-1):
            if m[i][j] != ' ':
                x = 10*x + int(m[i][j])
        nums.append(x)

    x = nums[0] 
    for i in range(1, len(nums)):
        if m[-1][op_idx] == '+':
            x += nums[i]
        else:
            x *= nums[i]
    ans += x
    
    last_op_idx = op_idx
    op_idx -= 1
    while op_idx >= 0 and m[-1][op_idx] == ' ':
        op_idx -= 1

print(ans)
