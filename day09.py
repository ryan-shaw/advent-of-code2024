from aoc import timer, read_raw_input

disk_map = read_raw_input(9).strip()


def expand_files(disk_map):
    for idx, value in enumerate(disk_map):
        if int(value) > 0:
            yield [idx // 2] * int(value) if idx % 2 == 0 else [None] * int(value)


def expand_blocks(disk_map):
    for idx, value in enumerate(disk_map):
        for _ in range(int(value)):
            yield idx // 2 if idx % 2 == 0 else None


def checksum(expanded):
    return sum([idx * value for idx, value in enumerate(expanded) if value != None])


@timer
def part1():
    expanded = list(expand_blocks(disk_map))
    replace_at = 0
    while True:
        while len(expanded) > 0 and (val := expanded.pop()) == None:
            pass

        try:
            replace_at = expanded.index(None, replace_at)
        except ValueError:
            expanded.append(val)
            break
        expanded[replace_at] = val

    return checksum(expanded)


part1()


@timer
def part2():
    expanded = list(expand_files(disk_map))
    head = len(expanded) - 1
    while True:
        head_val = expanded[head]
        if any([val == None for val in head_val]):
            head -= 1
            continue

        for idx, value in enumerate(expanded):
            if idx < head and len(value) >= len(head_val) and value[0] is None:
                expanded[idx] = head_val
                expanded[head] = [None] * len(head_val)
                diff = len(value) - len(head_val)
                if diff:
                    expanded.insert(idx + 1, [None] * diff)
                else:
                    head -= 1
                break
        else:
            head -= 1

        if head <= 0:
            break

    return checksum([val for sublist in expanded for val in sublist])


part2()
