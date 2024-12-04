from aoc import timer, read_input
import itertools

data = read_input(4)
data = [[c for c in line] for line in data]
count = 0

def find_in_direction(chars_to_find, y, x, pathy, pathx):
    if len(chars_to_find) == 0:
        return True
    if chars_to_find[0] == data[y+pathy][x+pathx] and y+pathy >= 0 and x+pathx >= 0:
        return find_in_direction(chars_to_find[1:], y+pathy, x+pathx, pathy, pathx)
    return False
    

def find_char_around(chars_to_find, y, x):
    if data[y][x] != 'X': return 0
    
    count = 0
    char = chars_to_find[0]
    for deltax, deltay in itertools.product(range(-1, 2), range(-1, 2)):
        if deltax == 0 and deltay == 0: continue
        try:
            if data[y+deltay][x+deltax] == char:
                if find_in_direction(chars_to_find[1:], y+deltay, x+deltax, deltay, deltax):
                    count += 1
        except IndexError:
            pass
    return count

@timer
def part1():
    count = 0
    count += sum(find_char_around(['M', 'A', 'S'], y, x) for y, row in enumerate(data) for x in range(len(row)))


    return count

part1()

def is_x(y, x):
    try:
        if data[y][x] != 'A': return 0
        if y == 0 or x == 0: return 0
        conditions = [
            data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S',
            data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M',
            data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M',
            data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S',
        ]
        result = any(conditions[:2]) and any(conditions[2:])
        return result
    except IndexError:
        return 0

@timer
def part2():
    return sum(is_x(y, x) for y, row in enumerate(data) for x in range(len(row)))

part2()
