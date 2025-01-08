import re

def extract_mul(mem):
    inst = re.findall(r"mul\(\d+,\d+\)", mem) #p1
    #inst = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", mem) #p2
    
    mul_enabled = True
    total_sum = 0

    
    for i in inst:
        match i:
            case "do()":
                mul_enabled = True
            case "don't()":
                mul_enabled = False
            case str(x) if 'mul' in x:
                x, y = map(int, re.findall(r'\d+', i))
                if mul_enabled:
                    total_sum += x * y

    return total_sum

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    data = read_input('input.txt')
    result = extract_mul(data)

    print(f"Sum: {result}")

if __name__ == '__main__':
    main()
