from pathlib import Path
txt = Path('input.txt').read_text()
list = txt.split('\n')

score = 0
for line in list:
    numbers = [(pos, num) for pos, num in enumerate(line) if num.isdigit()]
    first=(numbers[0][1])
    last=(numbers[len(numbers)-1][1])
    sum=first+last
    score= score+int(sum)
    print(score)

print("sum: ", score)
