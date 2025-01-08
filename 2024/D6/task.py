from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

def turn(facing):
    match facing:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP

def move(current, facing):
    match facing:
        case Direction.UP:
            return current[0] - 1, current[1]
        case Direction.RIGHT:
            return current[0], current[1] + 1
        case Direction.DOWN:
            return current[0] + 1, current[1]
        case Direction.LEFT:
            return current[0], current[1] - 1


def circle(grid, current, block, rows, cols, memo):
    if (current, block) in memo:
        return memo[(current, block)]

    grid = [list(row) for row in grid]  # mutable copy
    if block is not None:
        grid[block[0]] = ''.join(("#" if i == block[1] else x) for i, x in enumerate(grid[block[0]]))  # Add new obst

    facing = Direction.UP
    visited = set()

    while (current, facing) not in visited:
        visited.add((current, facing))
        proposed = move(current, facing)
        
        # check if out of bounds
        if proposed[0] < 0 or proposed[0] >= rows or proposed[1] < 0 or proposed[1] >= cols:
            memo[(current, block)] = False
            return False
        
        # collision
        while grid[proposed[0]][proposed[1]] == "#":
            facing = turn(facing)
            proposed = move(current, facing)
            if proposed[0] < 0 or proposed[0] >= rows or proposed[1] < 0 or proposed[1] >= cols:
                memo[(current, block)] = False
                return False

        current = proposed
    
    memo[(current, block)] = True  # loop detected
    return True

def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip("\n").split("\n")

def find_start_position(grid):
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            if x == "^":
                return (r, c)
    return None

def print_grid(grid):
    for row in grid:
        print(''.join(row))


def main():
    grid = read_input("input.txt")

    rows = len(grid)
    cols = len(grid[0])
    start = find_start_position(grid)

    current = start
    facing = Direction.UP
    visited = set()
    memo = {}

    while True:
        visited.add(current)
        proposed = move(current, facing)
        
        if proposed[0] < 0 or proposed[0] >= rows or proposed[1] < 0 or proposed[1] >= cols:
            break

        while grid[proposed[0]][proposed[1]] == "#":
            facing = turn(facing)
            proposed = move(current, facing)

        current = proposed

    p1 = len(visited)
    p2 = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != start:
                if circle(grid, start, (r, c), rows, cols, memo):
                    p2 += 1

    print(f"Result p1: {p1}")
    print(f"Result p2: {p2}")

if __name__ == "__main__":
    main()
