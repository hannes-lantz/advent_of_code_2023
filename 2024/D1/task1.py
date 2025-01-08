file_path = 'input.txt'


score = 0
left = []
right = []
diff = []

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        numbers = line.split()
        first = int(numbers[0])
        last = int(numbers[1])
        
        left.append(first)
        right.append(last)

left.sort()
right.sort()

for l, r in zip(left, right):
    d = max(l, r) - min(l, r)
    diff.append(d)
    score += d

print("sum: ", score)
