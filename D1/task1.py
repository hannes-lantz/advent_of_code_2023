from pathlib import Path
txt = Path('input.txt').read_text()

items = txt.replace('\n', ' ').split("  ")
max = 0
for i in items:
    bag = i.split(" ")
    res = [eval(j) for j in bag]
    if max < sum(res):
        max = sum(res)

print("Highest score is: ", max)
