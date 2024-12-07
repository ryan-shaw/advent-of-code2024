from aoc import timer, read_input

data = [[int(x) for x in l.split()] for l in read_input(2)]


def is_safe(raw_report):
    report = [level - raw_report[i + 1] for i, level in enumerate(raw_report[:-1])]
    return (all(x < 0 for x in report) or all(x > 0 for x in report)) and all(
        abs(x) < 4 for x in report
    )


@timer
def part1():
    return sum([is_safe(report) for report in data])


part1()


@timer
def part2():
    return sum(
        1
        for report in data
        if any(is_safe(report[:idx] + report[idx + 1 :]) for idx in range(len(report)))
        or is_safe(report)
    )


part2()
