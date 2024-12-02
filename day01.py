from aoc import timer, read_input
from collections import Counter

data = read_input(1)

l1, l2 = [], []
[(l1.append(int(c1)), l2.append(int(c2))) for c1, c2 in [line.split() for line in data]]

@timer
def part1():
    return sum([abs(z1 - z2) for z1, z2 in zip(sorted(l1), sorted(l2))])

part1()

@timer
def part2():
    c = Counter(l2)
    return sum(l * c[l] for l in l1)
        

part2()