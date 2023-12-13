from functools import cmp_to_key

f = open("input.txt", "r")
# f = open("i", "r")

data = f.read().split("\n")

strengths = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))

def classify(hand):
    frequencies = {}
    for c in hand:
        if c != "J":
            if c not in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1
    
    js = list(hand).count("J")
    most = None
    for f in frequencies:
        if most is None:
            most = f
        if frequencies[f] > frequencies[most]:
            most = f

    if most is None:
        return 7
    print(most, hand, frequencies)
    frequencies[most] += js
    a = []
    for f in frequencies:
        a.append(frequencies[f])
    
    
    if 5 in a:
        return 7
    if 4 in a:
        return 6
    if 3 in a:
        if 2 in a:
            return 5
        return 4
    if 2 in a:
        if a.count(2) == 2:
            return 3
        return 2
    return 1
    

    

def compare_hands(h1, h2):
    c1 = classify(h1)
    c2 = classify(h2)
    if c1 != c2:
        if c1 < c2:
            return -1
        if c1 == c2:
            return 0
        return 1
    
    for i in range(5):
        if h1[i] != h2[i]:
            if strengths.index(h1[i]) < strengths.index(h2[i]):
                return -1
            if strengths.index(h1[i]) > strengths.index(h2[i]):
                return 1


# def compare(h1, h2):
#     if compare_hands(h1, h2):
#         return -1
#     elif compare_hands(h1) > compare_hands(h2):
#         return 1
#     else:
#         return 0

hand_to_bid = {}
hands = []

for line in data:
    hand, bid = line.split(" ")
    hands.append(hand)
    hand_to_bid[hand] = int(bid)


# hands = sorted(hands, key=compare_hands)
hands = sorted(hands, key=cmp_to_key(compare_hands))
print(hands)

result = 0
for i in range(len(hands)):
    print((i + 1), hands[i], hand_to_bid[hands[i]], classify(hands[i]))
    result += (i + 1) * hand_to_bid[hands[i]]



print(result)


f.close()