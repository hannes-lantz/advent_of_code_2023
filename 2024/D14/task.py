import re

def read_input(filepath):
    with open(filepath) as f:
        return f.read().split('\n')

def extract_ints(line):
    return list(map(int, re.findall(r"((?:-|\+)?\d+)", line)))

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def part1(robots_info):
    matrix = []
    rows, cols = 101, 103

    for i in range(rows):
        matrix.append([0] * cols)

    for robot_info in robots_info:
        x, y, dx, dy = extract_ints(robot_info)
        
        matrix[x][y] += 1

        for _ in range(100):
            matrix[x][y] -= 1
            nx, ny = x + dx, y + dy

            if not is_valid(nx, ny, rows, cols):
                nx = (x + dx) % rows
                ny = (y + dy) % cols

            matrix[nx][ny] += 1
            x, y = nx, ny

    first_quarter = 0
    for i in range(rows // 2):
        for j in range(cols // 2):
            if i != rows // 2 and j != cols // 2:
                first_quarter += matrix[i][j]

    second_quarter = 0
    for i in range(rows // 2):
        for j in range(cols // 2, cols):
            if i != rows // 2 and j != cols // 2:
                second_quarter += matrix[i][j]

    third_quarter = 0
    for i in range(rows // 2, rows):
        for j in range(cols // 2):
            if i != rows // 2 and j != cols // 2:
                third_quarter += matrix[i][j]

    fourth_quarter = 0
    for i in range(rows // 2, rows):
        for j in range(cols // 2, cols):
            if i != rows // 2 and j != cols // 2:
                fourth_quarter += matrix[i][j]

    return first_quarter * second_quarter * third_quarter * fourth_quarter

def part2(robots_info):
    rows, cols = 101, 103
    robots_info = [(x, y, dx, dy) for x, y, dx, dy in map(extract_ints, robots_info)]

    ans = 0

    while True:
        ans += 1
        pos = set()

        for i in range(len(robots_info)):
            x, y, dx, dy = robots_info[i]
            nx = (x + dx) % rows
            ny = (y + dy) % cols
            pos.add((nx, ny))
            robots_info[i] = (nx, ny, dx, dy)

        if len(pos) == len(robots_info):
            break

    return ans

def main():
    robots_info = read_input('input.txt')
    p1 = part1(robots_info)
    p2 = part2(robots_info)

    print(f'p1: {p1}')
    print(f'p2: {p2}')

if __name__ == '__main__':
    main()