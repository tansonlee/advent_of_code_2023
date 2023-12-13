from functools import lru_cache

f = open("input.txt")
lines = f.read().split("\n")

@lru_cache(maxsize=None)
def score_num(num):
    line = lines[num - 1]
    line = line.strip()

    start = line.find(":") + 1
    win, have = line[start:].split("|")
    win.strip()
    have.strip()
    win = win.split(" ")
    have = have.split(" ")

    score = 0
    for w in win:
        if w == '':
            continue
        if w in have:
            score += 1
    print(num, score)
    for i in range(score):
        score += score_num(num + 1 + i)
    
    return score

def main():
    result = 0
    cards = [i + 1 for i in range(len(lines))]
    result += len(cards)
    for c in cards:
        result += score_num(c)
    print(result)

# def main():
#     result = 0
#     c = {}
#     with open("input.txt") as f:
#         lines = f.read().split("\n")
#         cards = [i + 1 for i in range(len(lines))]
#         result += len(cards)
#         while len(cards):
#             num = cards.pop(0)
#             line = lines[num - 1]
#             line = line.strip()

#             start = line.find(":") + 1
#             win, have = line[start:].split("|")
#             win.strip()
#             have.strip()
#             win = win.split(" ")
#             have = have.split(" ")

#             score = 0
#             for w in win:
#                 if w == '':
#                     continue
#                 if w in have:
#                     score += 1
#             print(num, score)
#             result += score
#             c[num] = score
#             for i in range(score):
#                 cards.append(num + 1 + i)
    
#     print(result)




main()