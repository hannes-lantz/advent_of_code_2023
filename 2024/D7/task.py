from itertools import product

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def concat(x, y):
    return int(str(x) + str(y))

OPERATORS = {'+': add, '*': multiply, '||': concat}

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        operator = operators[i - 1]
        result = OPERATORS[operator](result, numbers[i])
    return result

def main():
    total_sum = 0
    with open("input.txt") as f:
        for line in f:
            parts = line.strip().split(": ")
            test_value = int(parts[0])
            numbers = list(map(int, parts[1].split()))

            num_operators = len(numbers) - 1
            operator_combinations = product(['+', '*', '||'], repeat=num_operators)

            valid = False
            for operators in operator_combinations:
                if evaluate_expression(numbers, operators) == test_value:
                    valid = True
                    break

            if valid:
                total_sum += test_value

    print(total_sum)

if __name__ == "__main__":
    main()
