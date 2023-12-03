import re

input = open("./day2-input.txt")

part1total = 0
part2total = 0
redMax = 12
greenMax = 13
blueMax = 14

for game in input:
    valid = True
    red = 0
    green = 0
    blue = 0
    highestRed = 0
    highestGreen = 0
    highestBlue = 0

    gameId = int(re.search(r"\d+", game.split(": ")[0])[0])
    
    rounds = game.split(": ")[1] \
                 .split("; ")
    for round in rounds:
        cubes = re.findall(r"(\d+) (red|blue|green)", round)
        for x in cubes:
            if x[1] == 'red':
                red = int(x[0])
            elif x[1] == 'green':
                green = int(x[0])
            elif x[1] == 'blue':
                blue = int(x[0])
        if red > redMax or green > greenMax or blue > blueMax:
            valid = False
        if red > highestRed:
            highestRed = red
        if green > highestGreen:
            highestGreen = green
        if blue > highestBlue:
            highestBlue = blue
    if valid:
        part1total += gameId
    part2total += highestRed * highestGreen * highestBlue

print(part1total)
print(part2total)    
input.close()