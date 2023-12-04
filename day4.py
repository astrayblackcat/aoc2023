import re

with open('input.txt') as input_file:
    input = [line for line in input_file.read().strip().splitlines()]

winningRe = r"Card\s+\d+:((\s+\d+)+)+ \|((\s+\d+)+)+"
output = 0
copies = [1] * len(input)

for i, card in enumerate(input):
    winningNums = re.match(winningRe, card).group(1).split()
    selectedNums = re.match(winningRe, card).group(3).split()
    overlap = set(winningNums) & set(selectedNums)
    output += 2 ** len(overlap) // 2  
    for j in range(i+1, i+1+len(overlap)):
        copies[j] += copies[i]

print(output, sum(copies))
