f = open("test", "r")
data = f.read().split("\n")
data = [l.split(" ") for l in data]
data = [(a, int(b), c) for a, b, c in data]
f.close() 

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

print(data)

def pp(a):
    for x in a:
        print(*x)

min_rows = float("inf")
max_rows = 0
min_cols = float("inf")
max_cols = 0

curr = [0, 0]
for direction, n, _ in data:
    if direction == "U":
        curr[0] -= n
    elif direction == "D":
        curr[0] += n
    elif direction == "L":
        curr[1] -= n
    elif direction == "R":
        curr[1] += n
    
    min_rows = min(min_rows, curr[0])
    max_rows = max(max_rows, curr[0])

    min_cols = min(min_cols, curr[1])
    max_cols = max(max_cols, curr[1])

print(min_rows, max_rows, min_cols, max_cols)

def coord_to_ind(x, y):
    return x - min_rows, y - min_cols

grid = [["." for _ in range(max_cols - min_cols + 1)] for _ in range(max_rows - min_rows + 1)]


curr = [0, 0]
for direction, n, _ in data:
    print(curr)
    if direction == "U":
        for i in range(n):
            curr[0] -= 1
            row, col = coord_to_ind(curr[0], curr[1])
            grid[row][col] = "^"
    elif direction == "D":
        for i in range(n):
            curr[0] += 1
            row, col = coord_to_ind(curr[0], curr[1])
            grid[row][col] = "v"
    elif direction == "L":
        for i in range(n):
            curr[1] -= 1
            row, col = coord_to_ind(curr[0], curr[1])
            grid[row][col] = "<"
    elif direction == "R":
        for i in range(n):
            curr[1] += 1
            row, col = coord_to_ind(curr[0], curr[1])
            grid[row][col] = ">"

def dfs(row, col):
    if grid[row][col] == "#":
        return
    
    stack = [(row, col)]

    while stack:
        curr = stack.pop()
        if curr[0] < 0 or curr[1] < 0 or curr[0] >= len(grid) or curr[1] >= len(grid[0]):
            continue
        if grid[curr[0]][curr[1]] != ".":
            continue
        grid[curr[0]][curr[1]] = "#"

        stack.append((curr[0] + 1, curr[1]))
        stack.append((curr[0] - 1, curr[1]))
        stack.append((curr[0], curr[1] + 1))
        stack.append((curr[0], curr[1] - 1))

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "v":
            dfs(row, col - 1)

# for row in range(len(grid)):
#     inside = False
#     col = 0
#     while col < len(grid[row]):
#         if grid[row][col] != ".":
#             while col < len(grid[row]) and grid[row][col] != ".":
#                 col += 1
#             col -= 1
#             inside = not inside
#         elif inside:
#             grid[row][col] = "#"
#         col += 1

result = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != ".":
            result += 1

pp(grid)
print(result)


