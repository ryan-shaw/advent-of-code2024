from aoc import timer, read_input
from tqdm import tqdm
from itertools import product

equations = read_input(7)
equations = [(int(value), list(map(int, components.strip().split(' ')))) for (value, components) in [eq.split(':') for eq in equations]]

def evaluate_expression(components, operators):
    result = components[0]
    for i, operator in enumerate(operators):
        if operator == '*':
            result *= components[i + 1]
        elif operator == '+':
            result += components[i + 1]
        elif operator == '||':
            result = int(str(result) + str(components[i + 1]))
    return result

def is_equation_true(target, components, operators=['*', '+']):
    for op_comb in product(operators, repeat=len(components) - 1):
        if evaluate_expression(tuple(components), op_comb) == target:
            return target
    return 0

@timer
def part1():
    return sum([is_equation_true(value, components) for value, components in equations])

part1()

@timer
def part2():
    total = 0
    for i in tqdm(range(len(equations))):
        value = equations[i][0]
        components = equations[i][1]
        if v := is_equation_true(value, components, operators=['*', '+', '||']):
            total += v
        
    return total

part2()
