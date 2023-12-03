input = open("./day1-input.txt")

part1total = 0
part2total = 0

def getNumbers(str):
    first = -1
    second = 0
    for char in str:
        if char.isnumeric():
            if first < 0:
                first = int(char)
            second = int(char)
    return first * 10 + second
        
        
for string in input:
    part1total = getNumbers(string)
    part2string = string.replace("one", "one1one") \
                        .replace("two", "two2two") \
                        .replace("three", "three3three") \
                        .replace("four", "four4four") \
                        .replace("five", "five5five") \
                        .replace("six", "six6six") \
                        .replace("seven", "seven7seven") \
                        .replace("eight", "eight8eight") \
                        .replace("nine", "nine9nine")    
    part2total += getNumbers(part2string)

print(part1total)
print(part2total)
input.close()
        