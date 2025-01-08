from collections import deque

def bfs(grid, x, y, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    scale_top = 0

    while queue:
        x, y, height = queue.popleft()
        
        if height == 9:
            scale_top += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                if grid[nx][ny] == height + 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, height + 1))
    
    return scale_top

def dfs(grid, x, y, visited, rows, cols):
    if (x, y) in visited:
        return visited[(x, y)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    if grid[x][y] == 9:
        return 1
    
    total_paths = 0
  
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == grid[x][y] + 1:
                total_paths += dfs(grid, nx, ny, visited, rows, cols)
    
    visited[(x, y)] = total_paths
    return total_paths

def read_input(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def sum(grid):
    rows, cols = len(grid), len(grid[0])
    total_score = 0
    total_rating = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                total_score += bfs(grid, x, y, rows, cols)
                total_rating += dfs(grid, x, y, {}, rows, cols)
    
    return total_score, total_rating

def main():
    map = read_input('input.txt')
    score, rating = sum(map)
    print("Total Score:", score)
    print("Total Rating:", rating)

if __name__ == '__main__':
    main()