from aoc import timer, read_grid
from collections import defaultdict
from itertools import combinations

max_x, max_y, source_grid = read_grid(8)
for k, v in source_grid.items():
    if v == "#":
        source_grid[k] = "."


def print_grid(g):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(g[(x, y)], end="")
        print()


def in_bounds(loc):
    if loc[0] >= 0 and loc[0] <= max_x and loc[1] >= 0 and loc[1] <= max_y:
        return True


def get_locs(grid) -> dict:
    locs = defaultdict(list)
    antenna_count = 0
    for loc, antenna in grid.items():
        if antenna not in (".", "#"):
            locs[antenna].append(loc)
            antenna_count += 1
    return antenna_count, locs


@timer
def part1():
    grid = source_grid.copy()
    _, locs = get_locs(grid)
    unique_locs = set()
    for loc in locs.values():
        for comb in combinations(loc, 2):
            diff = tuple((y - x) for x, y in zip(*comb))
            a1 = tuple(y - x for x, y in zip(diff, comb[0]))
            a2 = tuple(x + y for x, y in zip(diff, comb[1]))
            if in_bounds(a1):
                unique_locs.add(a1)
                grid[a1] = "#"
            if in_bounds(a2):
                unique_locs.add(a2)
                grid[a2] = "#"
    print_grid(grid)
    return len(unique_locs)


part1()


@timer
def part2():
    grid = source_grid.copy()
    antenna_count, locs = get_locs(grid)
    unique_locs = set()

    def get_anitnodes(diff, start_node, opposite):
        antenna_count = 0
        while True:
            if not opposite and not in_bounds(
                start_node := tuple(y - x for x, y in zip(diff, start_node))
            ):
                break
            if opposite and not in_bounds(
                start_node := tuple(x + y for x, y in zip(diff, start_node))
            ):
                break
            if grid[start_node] not in (".", "#") and start_node not in unique_locs:
                antenna_count += 1
            unique_locs.add(start_node)
            grid[start_node] = "#"

        return antenna_count

    for loc in locs.values():
        for comb in combinations(loc, 2):
            diff = tuple((y - x) for x, y in zip(*comb))
            a1 = comb[0]
            a2 = comb[1]
            antenna_count -= get_anitnodes(diff, a1, False)
            antenna_count -= get_anitnodes(diff, a2, True)

    print_grid(grid)
    return len(unique_locs) + antenna_count


part2()
