from collections import defaultdict, deque

def check_update_order(rules, update):

    page_indices = {page: i for i, page in enumerate(update)}
    
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in page_indices and y in page_indices:
            if page_indices[x] > page_indices[y]:
                return False
    return True

def topological_sort(rules, update):
    
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in update and y in update:
            adj_list[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def solve(input, in_order):
   
    rules = input[0].splitlines()
    update_lines = input[1].splitlines()
    updates = [list(map(int, update.split(','))) for update in update_lines]

    sum_of_middle_pages = 0

    for update in updates:
        if in_order and check_update_order(rules, update):
            ordered_update = topological_sort(rules, update)
            middle_page = ordered_update[len(ordered_update) // 2]
            sum_of_middle_pages += middle_page
            
        if not in_order and not check_update_order(rules, update):
            ordered_update = topological_sort(rules, update)
            middle_page = ordered_update[len(ordered_update) // 2]
            sum_of_middle_pages += middle_page

    return sum_of_middle_pages

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split("\n\n")


def main():
    input = read_input('input.txt')
    p1 = solve(input, in_order=True)
    p2 = solve(input, in_order=False)
    print(f"Result p1: {p1}")
    print(f"Result p2: {p2}")

if __name__ == '__main__':
    main()
