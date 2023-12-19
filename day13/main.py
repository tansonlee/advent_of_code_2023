f = open("input", "r")

data = [x.split("\n") for x in f.read().split("\n\n")]
# data = [list(x) for x in data]

def pp(a):
    for x in a:
        print(x)

def find_horiz(pattern):
    for i in range(1, len(pattern)):
        check_dist = min(i, len(pattern) - i)

        errors = 0
        for row in range(i - check_dist, i):
            for col in range(len(pattern[row])):
                if pattern[row][col] != pattern[row + 2 * (i - row) - 1][col]:
                    # print(i, "error in: ", row, col)
                    errors += 1

        if errors == 1:
            return i
    return -1


def find_vert(pattern):
    for i in range(1, len(pattern[0])):
        check_dist = min(i, len(pattern[0]) - i)

        errors = 0
        for col in range(i - check_dist, i):
            for row in range(len(pattern)):
                if pattern[row][col] != pattern[row][col + 2 * (i - col) - 1]:
                    errors += 1
        if errors == 1:
            return i
    return -1

result = 0

for p in data:
    pp(p)
    a = find_horiz(p)
    if a != -1:
        print(a)
        result += 100 * a
        continue

    b = find_vert(p)
    if b != -1:
        print(b)
        result += b
        continue

    print("COULD NOT FIND A REFLECTION")

print(result)
f.close()
