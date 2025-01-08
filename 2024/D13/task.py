def read_input(file_path):
    with open(file_path) as f:
        return f.read()

def part1(data, prize_shift = 0):
    machines = data.split("\n\n")
    mach = []
    for machine in machines:
        a, b, prize = machine.splitlines()
        p = a.split("+")
        ax = int(p[1].split(",")[0])
        ay = int(p[2])
        p = b.split("+")
        bx = int(p[1].split(",")[0])
        by = int(p[2])
        p = prize.split("=")
        px = int(p[1].split(",")[0]) + prize_shift
        py = int(p[2]) + prize_shift
        mach.append(((ax,ay),(bx,by),(px,py)))
    
    s = 0
    for ((ax,ay),(bx,by),(px,py)) in mach:
        m = (ax * py - ay * px)/(ax * by - ay * bx)
        n = (px - m * bx)/(ax)
        
        if int(m) == m and int(n) == n:
            s += int(m) + 3 * int(n)
    return s



def part2(data):
    return part1(data, prize_shift=10000000000000)

def main():
    input = read_input('input.txt')

    p1 = part1(input)
    p2 = part2(input)

    print(f"P1: {p1}")
    print(f"P2: {p2}")

if __name__ == "__main__":
    main()