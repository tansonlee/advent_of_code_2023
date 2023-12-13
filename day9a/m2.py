f = open("input", "r")

data = f.read().split("\n")
data = [list(s) for s in data]

start = None
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = (i, j)
        # Repair the map

def is_valid(pos):
    if pos[0] < 0 or pos[1] < 0:
        return False
    if pos[0] >= len(data) or pos[1] >= len(data[0]):
        return False
    return True

def get_after_start():
    down = (start[0] + 1, start[1])
    if is_valid(down) and data[down[0]][down[1]] in "|LJ":
        return down
    up = (start[0] - 1, start[1])
    if is_valid(up) and data[up[0]][up[1]] in "|7F":
        return up 
    left = (start[0], start[1] - 1)
    if is_valid(left) and data[left[0]][left[1]] in "-LF":
        return left 
    right = (start[0], start[1] + 1)
    if is_valid(right) and data[right[0]][right[1]] in "-J7":
        return right 



curr = get_after_start() 

path_len = 1

data[start[0]][start[1]] = 'X'
while True:
    possibilities = []
    curr_symbol = data[curr[0]][curr[1]]
    print(curr_symbol, curr)
    if curr_symbol == "|":
        possibilities.append((curr[0] - 1, curr[1]))
        possibilities.append((curr[0] + 1, curr[1]))
    if curr_symbol == "-":
        possibilities.append((curr[0], curr[1] - 1))
        possibilities.append((curr[0], curr[1] + 1))
    if curr_symbol == "L":
        possibilities.append((curr[0] - 1, curr[1]))
        possibilities.append((curr[0], curr[1] + 1))
    if curr_symbol == "J":
        possibilities.append((curr[0] - 1, curr[1]))
        possibilities.append((curr[0], curr[1] - 1))
    if curr_symbol == "7":
        possibilities.append((curr[0], curr[1] - 1))
        possibilities.append((curr[0] + 1, curr[1]))
    if curr_symbol == "F":
        possibilities.append((curr[0] + 1, curr[1]))
        possibilities.append((curr[0], curr[1] + 1))
    
    print(possibilities)

    got = False
    for nrow, ncol in possibilities:
        if is_valid((nrow, ncol)) and data[nrow][ncol] != "X":
            data[curr[0]][curr[1]] = "X"
            curr = (nrow, ncol)
            path_len += 1
            got = True
            break
    if not got:
        break

data[curr[0]][curr[1]] = 'X'


print(path_len)

def pretty_print(data):
    for lst in data:
        print(*lst)

# pretty_print(data)

result = 0

def dfs(row, col):
    global result
    visited = set()
    stack = [(row, col)]
    cumulative = 0
    while len(stack):
        curr = stack.pop()
        print(curr)
        if curr in visited:
            continue
        visited.add(curr)
        data[curr[0]][curr[1]] = "^"
        cumulative += 1
        possibilities = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for drow, dcol in possibilities:
            nrow = curr[0] + drow
            ncol = curr[1] + dcol
            if not is_valid((nrow, ncol)):
               return 
            if data[nrow][ncol] not in "X^":
                stack.append((nrow, ncol))
    result += cumulative


def inside(row, col):
    up = 0
    for i in range(row):
        if data[i][col] == "X":
            up += 1
    
    down = 0
    for i in range(row, len(data)):
        if data[i][col] == "X":
            down += 1
    
    left = 0
    for i in range(col):
        if data[row][i] == "X":
            left += 1
    
    right = 0
    for i in range(col, len(data[0])):
        if data[row][i] == "X":
            right += 1
    
    if up % 2 == 1 or down % 2 == 1 or left % 2 == 1 or right % 2 == 1:
        return False
    return True



# for i in range(len(data)):
#     for j in range(len(data[i])):
        # if data[i][j] not in 'X^':
            # print("DFS FROM", i, j)
            # pretty_print(data)
            # dfs(i, j)
        # if data[i][j] != "X" and inside(i, j):
        #     result += 1

f.close()
f = open("input", "r")
original = f.read().split("\n")
original = [list(s) for s in original]
new_data = [["." for _ in range(len(data[0]))] for _ in range(len(data))]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            new_data[i][j] = original[i][j]
pretty_print(new_data)


# repair the board
new_data[start[0]][start[1]] = "F"

for row in new_data:
    inside = False
    for i in range(len(row)):
        if row[i] in "|JL":
            inside = not inside
            continue
        if inside and row[i] == ".":
            result += 1
            row[i] = "^"


pretty_print(new_data)
print(result)

f.close()