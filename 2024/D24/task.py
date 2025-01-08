def load_circuit(data):
    wires = {}
    operations = []
    highest_z_wire = "z00"
    for line in parse_circuit_data(data):
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            input1, operator, input2, _, result = line.split(" ")
            operation = {
                "input1": input1,
                "operator": operator,
                "input2": input2,
                "result": result
            }
            operations.append(operation)
            if result.startswith('z'):
                current_z_value = int(result[1:])
                highest_z_value = int(highest_z_wire[1:])
                if current_z_value > highest_z_value:
                    highest_z_wire = result
    return wires, operations, highest_z_wire

def parse_circuit_data(data):
    return [line.strip() for line in data if line.strip()]

def execute_operation(op, val1, val2):
    match op:
        case "AND":
            return val1 & val2
        case "OR":
            return val1 | val2
        case "XOR":
            return val1 ^ val2

def identify_wrong_wires(operations, highest_z_wire):
    wrong_wires = set()
    for op in operations:
        if op["result"].startswith('z') and op["operator"] != "XOR" and op["result"] != highest_z_wire:
            wrong_wires.add(op["result"])
        if (op["operator"] == "XOR" and 
            not any(w.startswith(('x', 'y', 'z')) for w in [op["result"], op["input1"], op["input2"]])):
            wrong_wires.add(op["result"])
        if op["operator"] == "AND" and "x00" not in [op["input1"], op["input2"]]:
            for subop in operations:
                if ((op["result"] == subop["input1"] or op["result"] == subop["input2"]) 
                    and subop["operator"] != "OR"):
                    wrong_wires.add(op["result"])
        if op["operator"] == "XOR":
            for subop in operations:
                if ((op["result"] == subop["input1"] or op["result"] == subop["input2"]) 
                    and subop["operator"] == "OR"):
                    wrong_wires.add(op["result"])
    return wrong_wires

def process_circuit(wires, operations):
    while operations:
        op = operations.pop(0)
        if op["input1"] in wires and op["input2"] in wires:
            wires[op["result"]] = execute_operation(
                op["operator"],
                wires[op["input1"]],
                wires[op["input2"]]
            )
        else:
            operations.append(op)

def get_z_wire_value(wires):
    z_bits = [
        str(wires[wire])
        for wire in sorted(wires, reverse=True)
        if wire.startswith('z')
    ]
    return int("".join(z_bits), 2)

def read_input(file_path):
    with open(file_path) as f:
        return f.read().split("\n")

def main():
    data = read_input('input.txt')
    wires, operations, highest_z_wire = load_circuit(data)
    wrong_wires = identify_wrong_wires(operations, highest_z_wire)
    process_circuit(wires, operations)
    print(f"p1: {get_z_wire_value(wires)}")
    print(",".join(sorted(wrong_wires)))

if __name__ == "__main__":
    main()
