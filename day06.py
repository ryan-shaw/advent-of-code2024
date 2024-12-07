from aoc import timer, read_input

def find_start(grid):
    for coord, value in grid.items():
        if value == '^':
            return value, coord

def get_next_coord(direction, current_coord):
    if direction == '^':
        change = (0, -1)
    elif direction == '<':
        change = (-1, 0)
    elif direction == '>':
        change = (1, 0)
    elif direction == 'V':
        change = (0, 1)
    
    return (current_coord[0] + change[0], current_coord[1] + change[1])

def out_of_bounds(data, current_coord):
    return (current_coord[0] < 0 or current_coord[1] < 0 or current_coord[1] >= len(data) or current_coord[0] >= len(data[0]))

def rotate_guard(direction):
    values = ['^', '>', 'V', '<']
    return values[(values.index(direction) + 1) % 4]

@timer
def part1():
    
    data = read_input(6)
    grid = {}
    for y, line in enumerate(data):
        for x, v in enumerate(line):
            grid[(x ,y)] = v

    
    positions = set()
    direction, current_coord = find_start(grid)
    while not out_of_bounds(data, next_coord := get_next_coord(direction, current_coord)):
        if grid[next_coord] == '#':
            direction = rotate_guard(direction)
            continue
        current_coord = next_coord
        # if current_coord in positions:
        #     print("in")
        positions.add(current_coord)
    return len(positions)
    

def calculate_loops(data, grid_copy, direction, current_coord):
    positions = set()
    while not out_of_bounds(data, next_coord := get_next_coord(direction, current_coord)):
        if grid_copy[next_coord] == '#':
            direction = rotate_guard(direction)
            continue
        current_coord = next_coord
        if (direction, current_coord) in positions:
            return 1
        positions.add((direction, current_coord))
    return 0

@timer
def part2():
    
    data = read_input(6)
    grid = {}
    for y, line in enumerate(data):
        for x, v in enumerate(line):
            grid[(x ,y)] = v
    loops = 0
    start_direction, start_coord = find_start(grid)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if grid[(x ,y)] != '.':
                continue
        
            grid_copy = grid.copy()

            grid_copy[(x, y)] = '#'
            loops += calculate_loops(data, grid_copy, start_direction, start_coord)

    return loops
            


if __name__ == "__main__":
    part1()
    part2()
