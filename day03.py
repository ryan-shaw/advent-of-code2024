import re
from aoc import timer, read_input

data = read_input(3)


@timer
def part1():
    return sum(
        [
            sum([(int(a) * int(b)) for a, b in re.findall(r"mul\((\d+),(\d+)\)", line)])
            for line in data
        ]
    )


part1()


@timer
def part2():
    active = True
    output = 0
    for line in data:
        for match in re.finditer(r"mul\((\d+),(\d+)\)|(don\'t)\(\)|(do)\(\)", line):
            if match.group(4) == "do":
                active = True
            elif match.group(3) == "don't":
                active = False
            elif active:
                output += int(match.group(1)) * int(match.group(2))
    return output


part2()
