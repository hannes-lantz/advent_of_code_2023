def read_input(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    register_a = int(lines[0].split(":")[1].strip())
    register_b = int(lines[1].split(":")[1].strip())
    register_c = int(lines[2].split(":")[1].strip())

    
    program = list(map(int, lines[4].split(":")[1].strip().split(',')))

    return register_a, register_b, register_c, program


def execute_program(register_a, register_b, register_c, program):
    registers = {'A': register_a, 'B': register_b, 'C': register_c}

    ip = 0
    output = []

    
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:
            value = combo_operand_value(operand, registers)
            registers['A'] //= (2 ** value)

        elif opcode == 1:
            registers['B'] ^= operand

        elif opcode == 2:
            value = combo_operand_value(operand, registers)
            registers['B'] = value % 8

        elif opcode == 3:
            if registers['A'] != 0:
                ip = operand
                continue

        elif opcode == 4:
            registers['B'] ^= registers['C']

        elif opcode == 5:
            value = combo_operand_value(operand, registers)
            output.append(value & 7)

        elif opcode == 6:
            value = combo_operand_value(operand, registers)
            registers['B'] = registers['A'] // (2 ** value)

        elif opcode == 7:
            value = combo_operand_value(operand, registers)
            registers['C'] = registers['A'] // (2 ** value)

        ip += 2

    return output

def combo_operand_value(operand, registers):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']

def calculate_initial_value(program):
    reversed_program = program[::-1]
    initial_value = 0
    for digit in reversed_program:
        initial_value *= 8
        initial_value += digit
    return initial_value

def main():
    register_a, register_b, register_c, program = read_input()
    output = execute_program(register_a, register_b, register_c, program)
    result = ",".join(map(str, output))

    print(f"p1:, {result}")

    initial_value = calculate_initial_value(program)
    print(f"p2: {initial_value}")    


if __name__ == "__main__":
    main()