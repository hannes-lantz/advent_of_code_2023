from enum import IntEnum, StrEnum 

def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip().split('\n\n')
    
class obj(StrEnum):
    WALL = '#'
    BOX = 'O'
    ROBOT = '@'

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

dir = {
    '^': UP,
    '>': RIGHT,
    'v': DOWN,
    '<': LEFT,
    '\n': 0
}


def sum_box_gps(input, big_warehouse = False):
    grid, insts = input

    walls, boxes = set(), set()
    robot_xy = None
    for y, row in enumerate(grid.split('\n')):
        x = 0
        for _, cell in enumerate(row):
            xy = complex(x, y)
            x += 1
            if cell == obj.ROBOT:
                robot_xy = xy
            elif cell == obj.WALL:
                walls.add(xy)
            elif cell == obj.BOX:
                boxes.add(xy)
            if big_warehouse:
                x += 1
                if cell == obj.WALL:
                    walls.add(xy + RIGHT)

    for inst in insts:
        move = dir[inst]
        boxes_rhs = {box + RIGHT for box in boxes} if big_warehouse else set()
        boxes_to_move = set()
        hit_wall = False
        xy_to_check = {robot_xy + move}
        while xy_to_check:
            if xy_to_check & walls:
                hit_wall = True
                break
            xy_to_check = xy_to_check & (boxes | boxes_rhs)
            if big_warehouse and move in (UP, DOWN):
                xy_to_check |= {xy + RIGHT for xy in xy_to_check & boxes}
                xy_to_check |= {xy + LEFT for xy in xy_to_check & boxes_rhs}
            boxes_to_move |= xy_to_check & boxes
            xy_to_check = {xy + move for xy in xy_to_check}

        if not hit_wall:
            robot_xy += move
            boxes = (boxes - boxes_to_move) | {box + move for box in boxes_to_move}

    return sum([int(abs(box.real) + abs(box.imag) * 100) for box in boxes])


def main():
    input = read_input('input.txt')

    print(f'P1: {sum_box_gps(input)}')
    print(f'P2: {sum_box_gps(input, big_warehouse=True)}')

if __name__ == '__main__':
    main()