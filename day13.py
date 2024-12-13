# Linear equations
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
#
# 34a + 67b = 5400
# 94a + 22b = 8400

import re
import sympy as sp
from aoc import timer, read_raw_input

numbers = re.compile(
    r"Button A: X\+(\d{2}), Y\+(\d{2})\nButton B: X\+(\d{2}), Y\+(\d{2})\nPrize: X=(\d{3,5}), Y=(\d{3,5})"
)

data = read_raw_input(13)
a, b = sp.symbols("a,b")


@timer
def part1():
    matches = numbers.findall(data)
    total = 0
    for match in matches:
        ax, ay, bx, by, px, py = map(int, match)
        e1 = sp.Eq(ax * a + bx * b, px)
        e2 = sp.Eq(ay * a + by * b, py)
        result = sp.solve([e1, e2], (a, b))
        if (
            isinstance(result[a], sp.core.numbers.Integer)
            and isinstance(result[b], sp.core.numbers.Integer)
            and result[a] <= 100
            and result[b] <= 100
        ):
            total += result[a] * 3 + result[b]

    return total


@timer
def part2():
    matches = numbers.findall(data)
    total = 0
    for match in matches:
        ax, ay, bx, by, px, py = map(int, match)
        px += 10000000000000
        py += 10000000000000
        e1 = sp.Eq(ax * a + bx * b, px)
        e2 = sp.Eq(ay * a + by * b, py)
        result = sp.solve([e1, e2], (a, b))
        if isinstance(result[a], sp.core.numbers.Integer) and isinstance(
            result[b], sp.core.numbers.Integer
        ):
            total += result[a] * 3 + result[b]

    return total


if __name__ == "__main__":
    part1()
    part2()
