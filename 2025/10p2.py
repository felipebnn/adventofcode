#!/bin/env python3
import pulp

with open('10_input.txt', 'r') as f:
    txt = f.read().strip('\n')

def solve_min_sum_linear_system(buttons, joltages):
    p = pulp.LpProblem()

    # bounded decision variables - [0, max_joltage]
    variables = [
        pulp.LpVariable(str(i), lowBound=0, upBound=max(joltages), cat=pulp.LpInteger)
        for i in range(len(buttons))
    ]

    # add objective to be minimized - the sum of the variables
    p += pulp.lpSum(variables)

    # add constraints for each linear equation
    for i, joltage in enumerate(joltages):
        equation = pulp.lpSum(x for b, x in zip(buttons, variables) if i in b)
        p += equation == joltage

    p.solve(pulp.PULP_CBC_CMD(msg=0))

    return int(pulp.value(p.objective))

total = 0
for machine_str in txt.split('\n'):
    _, *buttons, joltages = machine_str.split(' ')
    buttons = [
        set(int(x) for x in button[1:-1].split(','))
        for button in buttons
    ]
    joltages = [
        int(j) for j in joltages[1:-1].split(',')
    ]

    total += solve_min_sum_linear_system(buttons, joltages)

print(total)
