#!/bin/env python3
import pulp

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

def solve_min_sum_linear_system(matrix, joltages):
    p = pulp.LpProblem('10p2', pulp.LpMinimize) 

    # bounded decision variables - [0, max_joltage]
    variables = [
        pulp.LpVariable(str(i), lowBound=0, upBound=max(joltages), cat=pulp.LpInteger)
        for i in range(len(matrix[0]))
    ]

    # add objective to be minimized - the sum of the variables
    p += pulp.lpSum(variables)

    # add constraints for each linear equation
    for coefficients, joltage in zip(matrix, joltages):
        equation = pulp.lpSum(x for x, c in zip(variables, coefficients) if c)
        p += equation == joltage

    p.solve(pulp.PULP_CBC_CMD(msg=0))

    return sum(int(pulp.value(x)) for x in variables)

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
    matrix = [
        [ i in button for button in buttons ]
        for i in range(len(joltages))
    ]

    total += solve_min_sum_linear_system(matrix, joltages)

print(total)
