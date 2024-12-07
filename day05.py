import functools
from aoc import timer, read_raw_input

data = read_raw_input(5).strip()

rules, update_list = data.split("\n\n")
rules = [tuple(map(int, rule.strip().split("|"))) for rule in rules.split("\n")]


# get which rules apply
def identify_rules(updates):
    for rule in rules:
        if rule[0] in updates and rule[1] in updates:
            yield rule


def check_rule(rule, updates):
    try:
        i0 = updates.index(rule[0])
        i1 = updates.index(rule[1])
    except ValueError:
        return
    if i0 > i1:  # not ok
        return rule


def check_update(updates):
    r = list(identify_rules(updates))
    for rule in r:
        out = check_rule(rule, updates)
        if out:
            return out
    return True


def check_correct(updates):
    out = check_update(updates)
    if out is not True:
        return out
    return True


def get_mid():
    for update_line in update_list.split("\n"):
        updates = list(map(int, update_line.split(",")))
        if check_correct(updates) is True:
            yield updates[len(updates) // 2]


@timer
def part1():
    return sum(get_mid())


part1()


def cmp(a, b):
    if (a, b) in rules:
        return -1
    elif (b, a) in rules:
        return 1
    return 0


def rule_update():
    for update_line in update_list.split("\n"):
        updates = list(map(int, update_line.split(",")))
        out = check_correct(updates)
        if out is not True:
            for rule in identify_rules(updates):
                if not check_rule(rule, updates):
                    continue
                updates = sorted(updates, key=functools.cmp_to_key(cmp))
            yield updates[len(updates) // 2]


@timer
def part2():
    return sum(rule_update())


part2()
