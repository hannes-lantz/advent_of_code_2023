from collections import Counter

def read_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip().split()))

def process_stone(stone):
    stone_str = str(stone)
    if stone == 0:
        return [1]
    elif len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    else:
        return [stone * 2024]

def blink(stones):
    new_stones = Counter()

    for stone, count in stones.items():
        for new_stone in process_stone(stone):
            new_stones[new_stone] += count
    return new_stones

def count_stones(input, blinks):
    stones = Counter(input)
    for _ in range(blinks):
        stones = blink(stones)
    return sum(stones.values())

def main():
    input = read_input("input.txt")

    p1 = count_stones(input, 25)
    print(f"Result p1: {p1}")

    p2 = count_stones(input, 75)
    print(f"Result p2: {p2}")

if __name__ == "__main__":
    main()