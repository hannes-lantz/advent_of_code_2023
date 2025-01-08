
def check_dir(x, y, dx, dy, input):
    if (input[x+dx][y+dy]     == 'M' and 
        input[x+2*dx][y+2*dy] == 'A' and 
        input[x+3*dx][y+3*dy] == 'S'):
        return 1
    else:
        return 0

def check_x_mas(x, y, input):
    count = 0

    # left
    if 3 <= x:
        count += check_dir(x, y, -1, 0, input)   # left
        if 3 <= y:
            count += check_dir(x, y, -1, -1, input)  # top-left
        if y <= len(input[0]) - 4:
            count += check_dir(x, y, -1, 1, input)   # top-right

    # right
    if x <= len(input) - 4:
        count += check_dir(x, y, 1, 0, input)
        if 3 <= y:
            count += check_dir(x, y, 1, -1, input)  # bottom-left
        if y <= len(input[0]) - 4:
            count += check_dir(x, y, 1, 1, input)   # bottom-right

    # down
    if 3 <= y:
        count += check_dir(x, y, 0, -1, input)

    # up
    if y <= len(input[0]) - 4:
        count += check_dir(x, y, 0, 1, input)

    return count

def count_xmas(input):
    total = 0
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == 'X':
                total += check_x_mas(x, y, input)
    return total

def check_x (x, y, input):
    xchars = [input[x+coord[0]][y+coord[1]] for coord in [(-1, -1), (-1, 1), (1, -1), (1, 1)]]
    if sorted(xchars) == ['M', 'M', 'S', 'S'] and input[x-1][y-1] != input[x+1][y+1]:
        return True
    return False

def count_x(input):
    total = 0
    for x in range(1, len(input) - 1):
        for y in range(1, len(input[0]) - 1):
            if input[x][y] == 'A' and check_x(x, y, input):
                total += 1
    return total

def read_input(file_path):
    input_data = []
    with open(file_path, 'r') as file:
        for line in file:
            input_data.append(line.strip())
    return input_data


def main():
    input = read_input('input.txt')
    p1 = count_xmas(input)
    p2 = count_x(input)
    print(f"Total number of 'XMAS': {p1}")
    print(f"Total number of 'MAS X': {p2}")

if __name__ == '__main__':
    main()
