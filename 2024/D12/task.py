from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def point_to_string(x, y):
    return f"{x},{y}"

def string_to_point(s):
    x, y = map(int, s.split(','))
    return x, y

def flood(grid, start_x, start_y, char, visited, rows, cols):
    points = set()
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        key = point_to_string(x, y)
        if (x, y) in visited or not in_bounds(x, y, rows, cols) or grid[y][x] != char:
            continue
        visited.add((x, y))
        points.add(key)
        for dx, dy in DIRECTIONS:
            queue.append((x + dx, y + dy))
    return points

def find_regions(grid):
    visited, regions = set(), []
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            if (x, y) not in visited:
                points = flood(grid, x, y, grid[y][x], visited, rows, cols)
                if points:
                    regions.append({'char': grid[y][x], 'points': points})
    return regions

def calculate_perimeter(region, grid, rows, cols):
    perimeter = 0
    for x, y in (string_to_point(p) for p in region['points']):
        perimeter += sum(
            not in_bounds(x + dx, y + dy, rows, cols) or grid[y + dy][x + dx] != region['char']
            for dx, dy in DIRECTIONS
        )
    return perimeter

def count_straight_sections(region):
    points = [string_to_point(p) for p in region['points']]
    side_count = 0
    for dir_x, dir_y in DIRECTIONS:
        side = {
            point_to_string(x + dir_x, y + dir_y)
            for x, y in points
            if point_to_string(x + dir_x, y + dir_y) not in region['points']
        }
        to_remove = set()
        for point_str in side:
            px, py = string_to_point(point_str)
            temp = (px + dir_y, py + dir_x)
            while point_to_string(temp[0], temp[1]) in side:
                to_remove.add(point_to_string(temp[0], temp[1]))
                temp = (temp[0] + dir_y, temp[1] + dir_x)
        side_count += len(side) - len(to_remove)
    return side_count

def total_fence_cost(grid, use_straight_sections=False):
    rows, cols = len(grid), len(grid[0])
    regions = find_regions(grid)
    return sum(
        len(region['points']) * (
            count_straight_sections(region)
            if use_straight_sections
            else calculate_perimeter(region, grid, rows, cols)
        )
        for region in regions
    )

def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f.readlines()]

def main():
    grid = read_input('input.txt')
    print(f"p1: {total_fence_cost(grid)}")
    print(f"p2: {total_fence_cost(grid, use_straight_sections=True)}")


if __name__ == "__main__":
    main()

