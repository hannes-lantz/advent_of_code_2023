def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip()

def parse_disk_map(disk_map):
    sizes = [int(x) for x in disk_map]
    blocks, file_id = [], 0
    for i, size in enumerate(sizes):
        blocks.extend([file_id] * size if i % 2 == 0 else ['.'] * size)
        if i % 2 == 0:
            file_id += 1
    return blocks

def compact_disk(blocks):
    blocks = blocks.copy()
    n = len(blocks)
    while True:
        right_pos = n - 1
        while right_pos >= 0 and blocks[right_pos] == '.':
            right_pos -= 1
        if right_pos < 0:
            break
        left_pos = 0
        while left_pos < n and blocks[left_pos] != '.':
            left_pos += 1
        if left_pos >= right_pos:
            break
        blocks[left_pos], blocks[right_pos] = blocks[right_pos], '.'
    return blocks

def find_file_info(blocks, file_id):
    start, size = None, 0
    for i, block in enumerate(blocks):
        if block == file_id:
            start = i if start is None else start
            size += 1
    return start, size

def find_leftmost_space(blocks, start_pos, required_size):
    current_size, start = 0, None
    for i in range(start_pos):
        if blocks[i] == '.':
            start = i if start is None else start
            current_size += 1
            if current_size == required_size:
                return start
        else:
            start, current_size = None, 0
    return None

def move_file(blocks, file_id):
    start, size = find_file_info(blocks, file_id)
    if start is None:
        return blocks
    new_start = find_leftmost_space(blocks, start, size)
    if new_start is None:
        return blocks
    new_blocks = blocks.copy()
    for i in range(start, start + size):
        new_blocks[i] = '.'
    for i in range(new_start, new_start + size):
        new_blocks[i] = file_id
    return new_blocks

def compact_disk_whole_files(blocks):
    max_file_id = max(block for block in blocks if block != '.')
    for file_id in range(max_file_id, -1, -1):
        blocks = move_file(blocks, file_id)
    return blocks

def calculate_checksum(blocks):
    return sum(pos * block for pos, block in enumerate(blocks) if block != '.')

def solve_p1(disk_map):
    blocks = parse_disk_map(disk_map)
    return calculate_checksum(compact_disk(blocks))

def solve_p2(disk_map):
    blocks = parse_disk_map(disk_map)
    return calculate_checksum(compact_disk_whole_files(blocks))

def main():
    disk_map = read_file('input.txt')
    p1 = solve_p1(disk_map)
    p2 = solve_p2(disk_map)
    print(f"p1 block-by-block checksum: {p1}")
    print(f"p2 whole-file checksum: {p2}")

if __name__ == "__main__":
    main()
