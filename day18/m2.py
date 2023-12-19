from itertools import pairwise

f = open("real", "r")
data = f.read().split("\n")
data = [l.split(" ") for l in data]
data = [(a, int(b), c) for a, b, c in data]
f.close() 

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

new_data = []

for _, _, c in data:
    num = c[2:7]
    num = int(num, 16)
    direction = int(c[7])
    if direction == 0:
        direction = "R"
    elif direction == 1:
        direction = "D"
    elif direction == 2:
        direction = "L"
    elif direction == 3:
        direction = "U"
    new_data.append((direction, num))
    
print(new_data)

points = []

path = 0
curr = [0, 0]
points.append(tuple(curr))
for direction, n in new_data:
    if direction == "U":
        curr[0] -= n
    elif direction == "D":
        curr[0] += n
    elif direction == "L":
        curr[1] -= n
    elif direction == "R":
        curr[1] += n
    else:
        print("INVALID DIRECTION")
    path += n
    points.append(tuple(curr))


# use trapezoid formula
area = 0
for i in range(len(points)):
    # area += (points[i][1] + points[(i + 1) % len(points)][1]) * (points[i][0] - points[(i + 1) % len(points)][0])
    area += (points[i][1] + points[(i + 1) % len(points)][1]) * (points[i][0] - points[(i + 1) % len(points)][0])
area /= 2



print(abs(area) + (path / 2) + 1)

# curr = [0, 0]
# for direction, n, _ in data:
#     print(curr)
#     if direction == "U":
#         for i in range(n):
#             curr[0] -= 1
#             row, col = coord_to_ind(curr[0], curr[1])
#             grid[row][col] = "^"
#     elif direction == "D":
#         for i in range(n):
#             curr[0] += 1
#             row, col = coord_to_ind(curr[0], curr[1])
#             grid[row][col] = "v"
#     elif direction == "L":
#         for i in range(n):
#             curr[1] -= 1
#             row, col = coord_to_ind(curr[0], curr[1])
#             grid[row][col] = "<"
#     elif direction == "R":
#         for i in range(n):
#             curr[1] += 1
#             row, col = coord_to_ind(curr[0], curr[1])
#             grid[row][col] = ">"

# def dfs(row, col):
#     if grid[row][col] == "#":
#         return
    
#     stack = [(row, col)]

#     while stack:
#         curr = stack.pop()
#         if curr[0] < 0 or curr[1] < 0 or curr[0] >= len(grid) or curr[1] >= len(grid[0]):
#             continue
#         if grid[curr[0]][curr[1]] != ".":
#             continue
#         grid[curr[0]][curr[1]] = "#"

#         stack.append((curr[0] + 1, curr[1]))
#         stack.append((curr[0] - 1, curr[1]))
#         stack.append((curr[0], curr[1] + 1))
#         stack.append((curr[0], curr[1] - 1))

# for row in range(len(grid)):
#     for col in range(len(grid[row])):
#         if grid[row][col] == "v":
#             dfs(row, col - 1)

# # for row in range(len(grid)):
# #     inside = False
# #     col = 0
# #     while col < len(grid[row]):
# #         if grid[row][col] != ".":
# #             while col < len(grid[row]) and grid[row][col] != ".":
# #                 col += 1
# #             col -= 1
# #             inside = not inside
# #         elif inside:
# #             grid[row][col] = "#"
# #         col += 1

# result = 0
# for row in range(len(grid)):
#     for col in range(len(grid[row])):
#         if grid[row][col] != ".":
#             result += 1

# pp(grid)
# print(result)


