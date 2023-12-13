f = open("input","r")

data = [list(x) for x in f.read().split("\n")]

def pretty_print(arr):
    for x in arr:
        print(*x)

for i in reversed(range(len(data))):
    if "#" not in data[i]:
        data.insert(i, ["." for _ in range(len(data[0]))])

for col in reversed(range(len(data[0]))):
    empty = True
    for row in range(len(data)):
        if data[row][col] == "#":
            empty = False
            break
    if not empty:
        continue

    for row in range(len(data)):
        data[row].insert(col, ".")

positions = []
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == "#":
            positions.append((row, col))

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

result = 0
for a in positions:
    for b in positions:
        if a != b:
            print(dist(a, b))
            result += dist(a, b)



pretty_print(data)

print(result)


f.close()