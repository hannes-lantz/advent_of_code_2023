def can_form_design(design, towel_patterns):
    dp = [False] * (len(design) + 1)
    dp[0] = True
    
    for i in range(1, len(design) + 1):
        for towel in towel_patterns:
            if i >= len(towel) and design[i-len(towel):i] == towel:
                dp[i] = dp[i] or dp[i - len(towel)]
    
    return dp[len(design)]

def count_possible_designs(designs, towel_patterns):
    possible_count = 0
    for design in designs:
        if can_form_design(design, towel_patterns):
            possible_count += 1
    return possible_count

def count_ways_to_construct(design, patterns, memo):
    if not design:
        return 1
    if design in memo:
        return memo[design]
    
    total_ways = 0

    for pattern in patterns:
        if design.startswith(pattern):
            total_ways += count_ways_to_construct(design[len(pattern):], patterns, memo)
    
    memo[design] = total_ways
    return total_ways

def total_number_of_ways(designs, towel_patterns):
    
    total_ways = 0
    for design in designs:
        memo = {}
        ways = count_ways_to_construct(design, towel_patterns, memo)
        total_ways += ways
        #print(f"Design '{design}' can be made in {ways} ways.")
    
    return total_ways

def read_input(file_path):
    with open(file_path) as file:
        return file.readlines()

def main():
    lines = read_input('input.txt')
    towel_patterns = lines[0].strip().split(", ")
    designs = [line.strip() for line in lines[2:] if line.strip()]
    
    print(f"p1:, {count_possible_designs(designs, towel_patterns)}")
    print(f"p2: {total_number_of_ways(designs, towel_patterns)}")    


if __name__ == "__main__":
    main()