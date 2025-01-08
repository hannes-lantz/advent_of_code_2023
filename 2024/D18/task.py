from collections import deque

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start, end):
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == end:
            return steps
        
        # Explore neighbors
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and grid[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    return -1  # no valid path

def simulate_falling_bytes(byte_positions):
    grid = [['.' for _ in range(71)] for _ in range(71)]
    
    return grid

def read_input(file_path):
    with open(file_path) as file:
            return [
                tuple(map(int, line.strip().split(',')))
                for line in file if line.strip()
            ]

def solve(input):
    grid = simulate_falling_bytes(input)
    start = (0, 0)
    end = (70, 70)
    
    print(f"p1: {bfs(grid, start, end)}")

    for i, (x, y) in enumerate(input):
        grid[x][y] = '#'
        
        if bfs(grid, start, end) == -1:
            return f"{x},{y}"

    return "No blockage detected"

def main():
    input = read_input('input.txt')
    p2 = solve(input)

    print(f"p2: {p2}")


if __name__ == "__main__":
    main()