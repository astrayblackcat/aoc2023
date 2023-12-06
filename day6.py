import math

with open('input.txt') as input:
    lines = [line.strip().split()[1:] for line in input]

p1times = [int(i) for i in lines[0]]
p1records = [int(i) for i in lines[1]]
p2time = int(''.join(lines[0]))
p2record = int(''.join(lines[1]))

numRecords = []

def getRecords(t, r):
    newRecords = []
    for i in range(1, t):
        dist = i * (t - i)
        if dist > r:
            newRecords.append(dist)
    return newRecords

for i in range(len(p1times)):
    numRecords.append(len(getRecords(p1times[i], p1records[i])))

print(math.prod(numRecords))
print(len(getRecords(p2time, p2record)))