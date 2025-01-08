def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]

def part1(lines):
    locks = []
    keys = []
    for i in range(len(lines) // 8 + 1):
        value = [0, 0, 0, 0, 0]
        for j in range(5):
            for k in range(5):
                if lines[i*8 + 1 + j][k] == '#':
                    value[k] = value[k] + 1
        if lines[i*8] == '#####':
            locks.append((value))
        if lines[i*8+6] == '#####':
            keys.append(value)

    pairs = 0
    for lock in locks:
        for key in keys:
            fit = True
            for k in range(5):
                if lock[k] + key[k] > 5:
                    fit = False
                    break
            if fit:
                pairs += 1
    return pairs

def main():
    input = read_input('input.txt')
    p1 = part1(input)

    print(f"P1: {p1}")

if __name__ == "__main__":
    main()