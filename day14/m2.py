import copy
f = open("in", "r")

data = f.read().split("\n")
data = [list(x) for x in data]


def transform_north(data):
    for col in range(len(data[0])):
        for row in range(1, len(data)):
            if data[row][col] == "O":
                data[row][col] = "."
                for new_row in reversed(range(row)):
                    if data[new_row][col] in "#O":
                        data[new_row + 1][col] = "O"
                        break
                    if new_row == 0:
                        data[0][col] = 'O'

def transform_south(data):
    for col in range(len(data[0])):
        for row in reversed(range(len(data) - 1)):
            if data[row][col] == "O":
                data[row][col] = "."
                for new_row in range(row, len(data)):
                    if data[new_row][col] in "#O":
                        data[new_row - 1][col] = "O"
                        break
                    if new_row == len(data) - 1:
                        data[len(data) - 1][col] = 'O'

    
def transform_west(data):
    for row in range(len(data)):
        for col in range(1, len(data[0])):
            if data[row][col] == "O":
                data[row][col] = "."
                for new_col in reversed(range(col)):
                    if data[row][new_col] in "#O":
                        data[row][new_col + 1] = "O"
                        break
                    if new_col == 0:
                        data[row][0] = 'O'

def transform_east(data):
    for row in range(len(data)):
        for col in reversed(range(len(data[0]) - 1)):
            if data[row][col] == "O":
                data[row][col] = "."
                for new_col in range(col, len(data[0])):
                    if data[row][new_col] in "#O":
                        data[row][new_col - 1] = "O"
                        break
                    if new_col == len(data[0]) - 1:
                        data[row][new_col] = "O"

def col_load(col):
    res = 0
    for row in range(len(data)):
        if data[row][col] == "O":
            res += len(data) - row
    
    return res


def north_weight(d):
    result = 0
    for col in range(len(d[0])):
        for row in range(len(d)):
            if d[row][col] == "O":
                result += len(d) - row
    return result

def pp(arr):
    for x in arr:
        print(*x)


prevs = []
head = 0

reps = 1000000000

for i in range(reps + 1):
    # prev = copy.deepcopy(data)
    transform_north(data)
    transform_west(data)
    transform_south(data)
    transform_east(data)
    
    t = tuple(map(tuple, data))
    if t in prevs:
        found = prevs.index(t)
        prevs = prevs[found:]
        head = found
        break
    prevs.append(t)

print(len(prevs))
final_state = prevs[((reps - 1 - head) % (len(prevs)))]

for x in prevs:
    print(north_weight(x))
    pp(x)
    print()

print(north_weight(final_state))
f.close()
