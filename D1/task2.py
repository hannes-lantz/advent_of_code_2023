import re

from pathlib import Path
txt = Path('input.txt').read_text()
list = txt.split('\n')

words = {
    "zero"  : 'zero0zero',
    "one"   : 'one1one',
    "two"   : 'two2two',
    "three" : 'three3three',
    "four"  : 'four4four',
    "five"  : 'five5five',
    "six"   : 'six6six',
    "seven" : 'seven7seven',
    "eight" : 'eight8eight',
    "nine"  : 'nine9nine'
}


score = 0
for line in list:
    for word in words:
        line = line.replace(word,words[word])
  
    numbers = [(pos, num) for pos, num in enumerate(line) if num.isdigit()]
    first=(numbers[0][1])
    last=(numbers[len(numbers)-1][1])
    sum=first+last
    score= score+int(sum)

print("sum: ", score)
