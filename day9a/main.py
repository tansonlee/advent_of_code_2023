f = open("i", "r")

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



prev = start
curr = get_after_start()

path_len = 1

while data[curr[0]][curr[1]] != "S":
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

    for nrow, ncol in possibilities:
        if is_valid((nrow, ncol)) and (nrow, ncol) != prev:
            print("chose", nrow, ncol)
            prev = curr
            curr = (nrow, ncol)
            path_len += 1
            break

        
print(path_len)


f.close()