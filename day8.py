import math
nodes = {}
currentNodes = []
with open('input.txt') as f:
        directions = f.readline().strip()
        for line in f:
            nodes[line[:3]] = (line[7:10], line[12:15])
            if line[2] == 'A':
                currentNodes.append(line[:3])

currentNode = 'AAA'
steps = 0
while currentNode != 'ZZZ':
    dir = directions[steps % len(directions)]
    if dir == 'L':
        currentNode = nodes[currentNode][0]
    elif dir == 'R':
        currentNode = nodes[currentNode][1]
    steps += 1

print(steps)

steps = [0] * len(currentNodes)
for node in range(len(currentNodes)):
     currentNode = currentNodes[node]

     while currentNode[2] != 'Z':
        dir = directions[steps[node] % len(directions)]
        if dir == 'L':
            currentNode = nodes[currentNode][0]
        elif dir == 'R':
            currentNode = nodes[currentNode][1]
        steps[node] += 1

print(math.lcm(*steps))