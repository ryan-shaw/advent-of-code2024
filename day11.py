from tqdm import tqdm
from aoc import timer, read_raw_input
from functools import cache

stones = [int(stone) for stone in read_raw_input(11).strip().split(" ")]


def apply_rules_p1(stones: list) -> list:
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            new_stones.append(int(str_stone[: len(str_stone) // 2]))
            new_stones.append(int(str_stone[len(str_stone) // 2 :]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


@timer
def part1():
    local_stones = stones.copy()
    for i in tqdm(range(6)):
        print(local_stones, len(local_stones), i)
        local_stones = apply_rules_p1(local_stones)

    return len(local_stones)


part1()


@cache
def apply_rules_p2(stone, blinks):
    if blinks == 0:
        return 1
    elif stone == 0:
        return apply_rules_p2(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        return apply_rules_p2(
            int(str_stone[: len(str_stone) // 2]), blinks - 1
        ) + apply_rules_p2(int(str_stone[len(str_stone) // 2 :]), blinks - 1)
    else:
        return apply_rules_p2(stone * 2024, blinks - 1)


@timer
def part2():
    local_stones = stones.copy()
    total = 0
    for stone in local_stones:
        count = apply_rules_p2(stone, 75)
        total += count
    return total


part2()
