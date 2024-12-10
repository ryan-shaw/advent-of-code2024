from aoc import timer, read_grid
from collections import deque

_, _, grid = read_grid(10, cast=int)


def bfs(grid, position):
    visited = set()
    queue = deque([(position, [position])])
    result = []

    while queue:
        current, path = queue.popleft()
        if grid[current] == 9:
            visited.add(current)
            result.append(path)
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (current[0] + dx, current[1] + dy)

            if new_pos in grid and new_pos not in path:
                if grid[new_pos] == grid[current] + 1:
                    queue.append((new_pos, path + [new_pos]))

    return len(visited), len(result)


@timer
def part1():
    return sum([bfs(grid, item[0])[0] for item in grid.items() if item[1] == 0])


part1()


@timer
def part2():
    return sum([bfs(grid, item[0])[1] for item in grid.items() if item[1] == 0])


part2()
