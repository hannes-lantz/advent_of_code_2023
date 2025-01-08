from functools import cache
from heapq import heappop, heappush



NORTH = (0, -1)
EAST  = (1, 0)
SOUTH = (0, 1)
WEST  = (-1, 0)

TURN_LEFT = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH
}

TURN_RIGHT = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}


def setup(input):
    global end_tile
    global walls

    walls = set()
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "S":
                start_tile = (x, y)
            elif c == "E":
                end_tile = (x, y)
            elif c == "#":
                walls.add((x, y))

    return start_tile 

@cache
def distance_to_end(xy, heading):
    y_distance = abs(end_tile[1] - xy[1])
    x_distance = abs(end_tile[0] - xy[0])
    distance = x_distance + y_distance
    if heading in (NORTH, SOUTH) and x_distance > 0:
        distance += 1000
    if heading in (EAST, WEST) and y_distance > 0:
        distance += 1000
    return distance

@cache
def possible_steps(xy, heading):
    to_left = (xy[0] + TURN_LEFT[heading][0], xy[1] + TURN_LEFT[heading][1])
    to_right = (xy[0] + TURN_RIGHT[heading][0], xy[1] + TURN_RIGHT[heading][1])
    next_xy = (xy[0] + heading[0], xy[1] + heading[1])
    next_steps = []
    if to_left not in walls:
        next_steps.append(((xy, TURN_LEFT[heading]), 1000))
    if to_right not in walls:
        next_steps.append(((xy, TURN_RIGHT[heading]), 1000))
    if next_xy not in walls:
        next_steps.append(((next_xy, heading), 1))
    return next_steps

def shortest_paths(start, heading):
    shortest_distance = 9223372036854775807
    visited = set()
    distance_to = {(start, heading): 0}
    visited_on_best_paths = set()
    to_visit = []
    heappush(to_visit, (distance_to_end(start, heading), (start, heading), []))
    while to_visit:
        _, this_state, path_here = heappop(to_visit)
        xy, heading = this_state
        if xy == end_tile:
            shortest_distance = distance_to[this_state]
            visited_on_best_paths |= set(path_here)
        visited.add(this_state)
        for next_state, step_cost in possible_steps(xy, heading):
            distance = distance_to[this_state] + step_cost
            if distance > shortest_distance:
                continue
            prior_distance = distance_to.get(next_state, 0)
            if next_state in visited and distance > prior_distance:
                continue
            if distance <= prior_distance or next_state not in [
                i[1] for i in to_visit
            ]:
                distance_to[next_state] = distance
                f_score = distance + distance_to_end(*next_state)
                next_path_here = path_here + [next_state[0]]
                heappush(to_visit, (f_score, next_state, next_path_here))

    return shortest_distance, visited_on_best_paths



def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()


def main():
    input = read_input('input.txt')
    start = setup(input)

    shortest_distance, visited_on_best_paths = shortest_paths(start, EAST)

    print(f'Part 1: {shortest_distance}')
    print(f'Part 2: {len(visited_on_best_paths)}')

if __name__ == '__main__':
    main()