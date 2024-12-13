from aoc import timer, read_grid
from collections import deque

_, _, grid = read_grid(12, cast=str)


def bfs(grid, position):
    visisted = set()
    queue = deque([(position, [position])])
    result = set()
    result.add(position)

    while queue:
        current, path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (current[0] + dx, current[1] + dy)
            if new_pos in visisted:
                continue
            visisted.add(new_pos)

            if new_pos in grid and new_pos not in path:
                if grid[new_pos] == grid[current]:
                    result.add(new_pos)
                    queue.append((new_pos, path + [new_pos]))

    return result


def neighbour_count(position, positions):
    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_pos = (position[0] + dx, position[1] + dy)
        if new_pos in positions:
            count += 1
    return count


def count_fences(positions):
    fence_total = 0
    for position in positions:
        neighbours = neighbour_count(position, positions)
        fences = 4 - neighbours
        fence_total += fences
    return fence_total


def get_positions():
    complete = set()
    for pos in grid.keys():
        if pos in complete:
            continue
        result = bfs(grid, pos)
        complete.update(result)
        yield result


def count_sides(result):
    # start by finding an edge to start on
    visited = set()
    direction = None
    position = list(result)[0]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_pos = (position[0] + dx, position[1] + dy)
        if new_pos not in result:
            direction = (dx, dy)
            break


@timer
def part1():
    total = 0
    for result in get_positions():
        fences = count_fences(result)
        cost = fences * len(result)
        total += cost

    return total


@timer
def part2():
    for result in get_positions():
        print(result)
        fences = count_sides(result)


if __name__ == "__main__":
    part1()
    part2()
