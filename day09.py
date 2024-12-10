
from aoc import timer, read_raw_input

disk_map = read_raw_input(9).strip()

def expand_files(disk_map):
    for idx, value in enumerate(disk_map):
        for _ in range(int(value)):
            yield idx//2 if idx % 2 == 0 else None

def checksum(expanded):
    return sum([idx * value for idx, value in enumerate(expanded) if value != None])

@timer
def part1():
    expanded = list(expand_files(disk_map))
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
