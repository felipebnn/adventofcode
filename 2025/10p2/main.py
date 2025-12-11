#!/bin/env python3
import pulp

with open('input.txt', 'r') as f:
    txt = f.read().strip('\n')

def solve_min_sum_linear_system(coefficients, joltages):
    num_equations = len(coefficients)
    num_variables = len(coefficients[0])

    p = pulp.LpProblem('10p2', pulp.LpMinimize) 

    # bounded decision variables - [0, max_joltage]
    variables = [
        pulp.LpVariable(str(i), lowBound=0, upBound=max(joltages), cat=pulp.LpInteger)
        for i in range(num_variables)
    ]

    # add objective to be minimized - the sum of the variables
    p += pulp.lpSum(variables)

    # add constraints for each linear equation
    for i in range(num_equations):
        equation = pulp.lpSum(a*b for a,b in zip(coefficients[i], variables))
        p += equation == joltages[i]

    p.solve(pulp.PULP_CBC_CMD(msg=0))

    return sum(int(pulp.value(variables[i])) for i in range(num_variables))

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
        [ 1 if i in buttons[j] else 0 for j in range(len(buttons)) ]
        for i in range(len(joltages))
    ]
    total += solve_min_sum_linear_system(matrix, joltages)

print(total)
