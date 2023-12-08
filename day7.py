from collections import Counter
with open('input.txt') as f:
    INPUT = [hand.strip().split() for hand in f]

P1SCORES = "23456789TJQKA"
P2SCORES = "J23456789TQKA"

handList = []
jokerList = []
total = 0

def joker(hand):
    count = Counter(hand[0])
    most = count.most_common()[0][0]
    if most == 'J' and hand[0] != 'JJJJJ':
        most = count.most_common()[1][0]
    return hand[0].replace('J', most)

def getValues(hand, wild=False):
    if not wild:
        handType = sorted(Counter(hand[0]).values())
        cardValues = [P1SCORES.index(i) for i in hand[0]]
    if wild:
        cardValues = [P2SCORES.index(i) for i in hand[0]]
        handType = sorted(Counter(joker(hand)).values())

    match handType:
        case [5]:
            handValue = 7
        case [1, 4]:
            handValue = 6
        case [2, 3]:
            handValue = 5
        case [1, 1, 3]:
            handValue = 4
        case [1, 2, 2]:
            handValue = 3
        case [1, 1, 1, 2]:
            handValue = 2
        case _:
            handValue = 1
    return handValue, cardValues

def getHandList(wild=False):
    for hand in INPUT:
        hand.append(getValues(hand, wild))
        handList.append(hand)

getHandList(True)
for hand_scores in list(enumerate(sorted(handList, key=lambda x: x[2]))):
    total += int(hand_scores[1][1]) * (hand_scores[0] + 1)

print(total)