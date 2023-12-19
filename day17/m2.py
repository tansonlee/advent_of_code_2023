from heapq import heappush, heappop

f = open("real", "r")
data = f.read().split("\n")
data = [list(map(int, list(x))) for x in data]
f.close()

total_cols = len(data[0])
total_rows = len(data)

# UP = 0
# RIGHT = 1
# DOWN = 2
# LEFT = 3

legal_moves = { (0,0): ((1, 0), (0, 1)),
                (0, -1) : ((1, 0), (-1, 0)),
                (1, 0): ((0, -1), (0, 1)),
                (0, 1): ((1, 0), (-1, 0)),
                (-1, 0): ((0, -1), (0, 1)) }


def pp(a):
    for x in a:
        print(*x)

def get_neighbors(node):
    row, col, direction, dir_steps = node
    result = []

    if direction == UP:
        result.append((row - 1, col, UP, dir_steps + 1))
        result.append((row, col + 1, RIGHT, 1))
        result.append((row, col - 1, LEFT, 1))
    elif direction == DOWN:
        result.append((row + 1, col, DOWN, dir_steps + 1))
        result.append((row, col + 1, RIGHT, 1))
        result.append((row, col - 1, LEFT, 1))
    elif direction == RIGHT:
        result.append((row, col + 1, RIGHT, dir_steps + 1))
        result.append((row - 1, col, UP, 1))
        result.append((row + 1, col, DOWN, 1))
    elif direction == LEFT:
        result.append((row, col - 1, LEFT, dir_steps + 1))
        result.append((row - 1, col, UP, 1))
        result.append((row + 1, col, DOWN, 1))

    if dir_steps == 3:
        same_dir_index = -1
        for i in range(len(result)):
            if result[i][2] == direction:
                same_dir_index = i
        if i == -1:
            print("BSBSDBDSBSDBDSB")
        
        del result[same_dir_index]
    
    for i in reversed(range(len(result))):
        curr = result[i]
        if curr[0] < 0 or curr[0] >= total_rows or curr[1] < 0 or curr[1] >= total_cols:
            del result[i]
    
    return result


def dijkstras():
    heap = [(0, (0, 0), (0, 0))]
    shortest_path = {}
    shortest_path[((0, 0), (0, 0))] = 0
    visited = set()
    
    # The algorithm executes until we visit all nodes
    while heap:
        # The code block below finds the node with the lowest score
        loss, coord, direction = heappop(heap)
        
        if coord == (total_rows - 1, total_cols - 1):
            break
        
        if (coord, direction) in visited:
            continue
        visited.add((coord, direction))

        for new_direction in legal_moves[direction]:
            new_loss = loss
            for steps in range(1, 11):
                new_coord = (coord[0] + steps * new_direction[0], coord[1] + steps * new_direction[1])
                if new_coord[0] < 0 or new_coord[1] < 0 or new_coord[0] >= total_rows or new_coord[1] >= total_cols:
                    continue
                new_loss += data[new_coord[1]][new_coord[0]]

                if steps >= 4:
                    new_node = (new_coord, new_direction)
                    if shortest_path.get(new_node, float("inf")) <= new_loss:
                        continue
                    shortest_path[new_node] = new_loss 
                    heappush(heap, (new_loss, new_coord, new_direction))

    print(loss)

    return shortest_path

paths = dijkstras()

# print(paths)
for p in paths:
    if p == (total_rows - 1, total_cols - 1):
        print(paths[p])



# from heapq import heappush, heappop
# from math import inf

# legal_moves = { (0,0): ((1, 0), (0, 1)),
#                 (0, -1) : ((1, 0), (-1, 0)),
#                 (1, 0): ((0, -1), (0, 1)),
#                 (0, 1): ((1, 0), (-1, 0)),
#                 (-1, 0): ((0, -1), (0, 1)) }

# def parts_is_parts(parts: str, mmin: int, mmax: int):
#     with open('test') as f:
#         grid = [[int(x) for x in line] for line in f.read().splitlines()]
#     destination_coord = (len(grid[0]) - 1, len(grid) - 1)
#     heap = [(0, (0,0), (0,0))]
#     heat_map = {(0,0): 0}
#     visited = set()

#     while heap:
#         heat_loss, coord, direction = heappop(heap)

#         if coord == destination_coord: 
#             break

#         if (coord, direction) in visited: continue
        
#         visited.add((coord, direction))

#         for new_direction in legal_moves[direction]:
#             new_heat_loss = heat_loss
#             for steps in range(1, mmax + 1):
#                 new_coord = (coord[0] + steps * new_direction[0], coord[1] + steps * new_direction[1])
#                 if new_coord[0] < 0 or new_coord[1] < 0 \
#                     or new_coord[0] > destination_coord[0] or new_coord[1] > destination_coord[1]:
#                     continue
#                 new_heat_loss = new_heat_loss + grid[new_coord[1]][new_coord[0]]
#                 if steps >= mmin:
#                     new_node = (new_coord, new_direction)
#                     if heat_map.get(new_node, inf) <= new_heat_loss: continue
#                     heat_map[new_node] = new_heat_loss
#                     heappush(heap, (new_heat_loss, new_coord, new_direction))
                    
#     print (parts, heat_loss)

# from timeit import Timer
# t = Timer(lambda: parts_is_parts("Part 1:",1,3))
# print(t.timeit(number=1))
# t = Timer(lambda: parts_is_parts("Part 2:",4,10))
# print(t.timeit(number=1))
