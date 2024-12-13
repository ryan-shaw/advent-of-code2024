import math
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
    for i in tqdm(range(25)):
        local_stones = apply_rules_p1(local_stones)

    return len(local_stones)


@cache
def calc_length(stone):
    return math.floor(math.log10(stone)) + 1


@cache
def split_stone(stone, length):
    divider = 10 ** (length // 2)
    left_half, right_half = divmod(stone, divider)
    return left_half, right_half


@cache
def apply_rules_p2(stone, blinks):
    if blinks == 0:
        return 1
    elif stone == 0:
        return apply_rules_p2(1, blinks - 1)
    elif (length := calc_length(stone)) % 2 == 0:
        left_half, right_half = split_stone(stone, length)
        return apply_rules_p2(left_half, blinks - 1) + apply_rules_p2(
            right_half, blinks - 1
        )
    else:
        return apply_rules_p2(stone * 2024, blinks - 1)


@timer
def part2():
    local_stones = stones.copy()
    total = 0
    for stone in local_stones:
        total += apply_rules_p2(stone, 75)

    return total


if __name__ == "__main__":
    part1()
    part2()
