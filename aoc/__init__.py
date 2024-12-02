import re
import sys
import time
from contextlib import contextmanager

DAY = int(re.match(r'^day(\d+).*', sys.argv[0]).group(1))

def read_input(name=DAY, cast=str):
    with open(f"inputs/input{name:02}") as f:
        content = f.readlines()
    return [cast(x.strip()) for x in content]

def read_raw_input(name=DAY):
    with open(f"inputs/input{name:02}") as f:
        content = f.read()
    return content

def read_test(index, name=DAY, cast=str):
    with open(f"tests/inputs/day{name:02}_{index}") as f:
        _input = [cast(x.strip()) for x in f.readlines()]
    with open(f"tests/expected/day{name:02}_{index}") as f:
        expected = [cast(x.strip()) for x in f.readlines()]
    return _input, expected

@contextmanager
def timerc():
    start_time = time.time()
    yield
    print(f"\nTime required: {(time.time() - start_time)*1000:.2f} ms\n")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time.time() - start_time)*1000:.2f} ms\n")
        print(f"Result: {result}")
        return result
    return wrapper