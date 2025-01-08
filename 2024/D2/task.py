def is_safe_report(levels):
    
    is_increasing = all(levels[i+1] - levels[i] >= 1 for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] - levels[i+1] >= 1 for i in range(len(levels) - 1))
    
    for i in range(len(levels) - 1):
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False
    
    return is_increasing or is_decreasing


def is_safe_with_one_removal(levels):
    
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        
        if is_safe_report(new_levels):
            return True
    
    return False


def count_safe_reports(data):
    safe_count = 0
    for report in data:
        if is_safe_report(report):
            safe_count += 1
        elif is_safe_with_one_removal(report):
            safe_count += 1
    return safe_count

def read_input(file_path):
    with open(file_path) as file:
        return [list(map(int, line.split())) for line in file]


def main():
    data = read_input('input.txt')
    safe_reports = count_safe_reports(data)
    print(f"Safe reports: {safe_reports}")

if __name__ == '__main__':
    main()
