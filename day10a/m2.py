f = open("input","r")

data = [list(x) for x in f.read().split("\n")]

curr_row_empty = 0
empty_rows = []

curr_col_empty = 0
empty_cols = []

def pretty_print(arr):
    for x in arr:
        print(*x)

for i in range(len(data)):
    if "#" not in data[i]:
        curr_row_empty += 1
    empty_rows.append(curr_row_empty)

for col in range(len(data[0])):
    empty = True
    for row in range(len(data)):
        if data[row][col] == "#":
            empty = False
            break
    if empty:
        curr_col_empty += 1
    empty_cols.append(curr_col_empty)

print(empty_rows)
print(empty_cols)

positions = []
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == "#":
            positions.append((row, col))

def dist(p1, p2):
    empty_rows_between = abs(empty_rows[p2[0]] - empty_rows[p1[0]])
    empty_cols_between = abs(empty_cols[p2[1]] - empty_cols[p1[1]])
    a = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + ((empty_rows_between + empty_cols_between) * 999999)
    # print(p1, p2, empty_rows_between, empty_cols_between, a)
    # print(p1, p2, a)
    return a


result = 0
for a in positions:
    for b in positions:
        result += dist(a, b)

pretty_print(data)
print(result)

f.close()