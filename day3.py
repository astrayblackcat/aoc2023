import re

dataArray = []
numbers = []
symbols = []
directions = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]
validNums = []
validGears = []

with open('day3-input.txt') as input:
    dataArray = [line.strip().split('\n') for line in input]

def getcoords(arr): #get number and symbol coords and store them in array
    for line in arr:
        nums = []
        syms = []
        for match in re.finditer(r"\d+", line[0]):
            nums.append(match)
        for match in re.finditer(r"[^0-9.]", line[0]):
            syms.append(match)
        numbers.append(nums)
        symbols.append(syms)

def getresults(syms):
    for i in range(len(syms)):
        for symbol in syms[i]:
            valid = []
            x1, x2 = symbol.span()
            for number in [number for sl in numbers[i - 1 : i + 2] for number in sl]:
                y1, y2 = number.span()
                if max(x1, y1) <= min(x2, y2):
                    validNums.append(int(number.group()))
                    valid.append(int(number.group()))
            if len(valid) == 2:
                validGears.append(valid[0] * valid[1])
                
getcoords(dataArray)
getresults(symbols)
print(sum(validNums))
print(sum(validGears))
input.close()